###########
# MODULES #
###########

# Python
import os
import pandas as pd
from tkinter import filedialog

# Third-Party
import customtkinter as ctk
from termcolor import colored

###########
# CLASSES #
###########

class ImportarDesdeArchivo:
    def __init__(self, path_archivo):
        self.path_archivo = path_archivo
    
    def getDatos(self):
        datos = pd.read_csv("notas_alumnos.csv", sep=";")
        return datos
    
class Estudiante:
    def __init__(self, nombre, nota_matematica, nota_ciencias, nota_lenguaje):
        self.nombre = nombre
        self.nota_matematica = nota_matematica
        self.nota_ciencias = nota_ciencias
        self.nota_lenguaje = nota_lenguaje
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Matematicas: {self.nota_matematica} - Ciencias: {self.nota_ciencias} - Lenguaje: {self.nota_lenguaje}"
    
    @property
    def calcular_promedio(self):
        self.promedio = (self.nota_matematica + self.nota_ciencias + self.nota_lenguaje) / 3
        return self.promedio
    
    @property
    def situacion_academica(self):
        if self.promedio >= 6:
            return "Aprobado/a"
        else:
            return "Reprobado/a"

#############
# FUNCTIONS #
#############

def ejecutar_proceso():
    global GB_FILE_PATH_INPUT
    global GB_FILE_PATH_OUTPUT

    # Importamos los datos generales de los estudiantes desde el archivo csv
    datos = ImportarDesdeArchivo(GB_FILE_PATH_INPUT)
    df_datos = datos.getDatos()
    
    # Mostramos en consola los datos importados
    print()
    print(colored("DATOS GENERALES IMPORTADOS DE LOS ESTUDIANTES:", "yellow"))
    print(df_datos)
    print()
    
    # Agregamos al dataframe las columnas "Promedio" y "Situacion_Academica"
    # Para generar después un nuevo archivo csv con la información completada
    df_datos["Promedio"] = ""
    df_datos["Situacion_Academica"] = ""
    
    # Generamos una instancia de la clase Estudiante para cada estudiante
    for index, row in df_datos.iterrows():
        
        # Aislamos los datos de cada Estudiante para generar la instancia
        nombre = df_datos["Estudiante"][index]
        nota_matematica = df_datos["Matematicas"][index]
        nota_ciencas = df_datos["Ciencias"][index]
        nota_lenguaje = df_datos["Lenguaje"][index]
        estudiante = Estudiante(nombre, nota_matematica, nota_ciencas, nota_lenguaje)
        
        # Calculamos el promedio y definimos la situación académica de cada estudiante
        promedio = estudiante.calcular_promedio
        situacion_academica = estudiante.situacion_academica
        
        # Mostramos la información en consola
        print(colored(f"ESTUDIANTE n°{index + 1}", "yellow"))
        print(f"    > {estudiante}")
        print(f"    > Promedio: {promedio:.2f}")
        print(f"    > Situación Académica: {situacion_academica}")
        print()
        
        # Actualizamos los datos generales de los estudiantes
        # Agregamos el promedio y la situación académica      
        df_datos.loc[index, "Promedio"] = round(promedio, 2)
        df_datos.loc[index, "Situacion_Academica"] = situacion_academica
    
    # Mostramos en consola los datos modificados
    print(colored("DATOS GENERALES ACTUALIZADOS DE LOS ESTUDIANTES:", "yellow"))
    print(df_datos)
    print()
    
    # Guardamos en un archivo csv los datos modificados
    df_datos.to_csv(GB_FILE_PATH_OUTPUT.get(), index=False, sep=";")
    
    # Mensaje de confirmación de final de proceso en consola
    print(f"El archivo de resumen de la evaluación de los estudiantes se ha guardado en: ")
    print(colored(f"    > {GB_FILE_PATH_OUTPUT.get()}", "green"))

def buscar_archivo_entrada():
    global GB_FILE_PATH_INPUT
    file_path_input = filedialog.askopenfilename()
    GB_FILE_PATH_INPUT.delete(0, ctk.END)
    GB_FILE_PATH_INPUT.insert(0, file_path_input)
    print("**********")
    print("Archivo de Entrada: ", GB_FILE_PATH_INPUT.get())
    print("**********")
    
def definir_archivo_salida():
    global GB_FILE_PATH_OUTPUT
    file_path_output = filedialog.asksaveasfilename(initialfile = "notas_alumnos_actualizadas.csv", title = "Select file", filetypes = (("csv files","*.csv"),))
    GB_FILE_PATH_OUTPUT.delete(0, ctk.END)
    GB_FILE_PATH_OUTPUT.insert(0, file_path_output)
    print("**********")
    print("Archivo de Salida: ", GB_FILE_PATH_OUTPUT.get())
    print("**********")


#################
# GLOBAL VALUES #
#################

GB_FILE_PATH_INPUT = ""
GB_FILE_PATH_OUTPUT = ""


########
# MAIN #
########
    
if __name__ == "__main__":
    
    # Crear la ventana de la interfaz gráfica
    root = ctk.CTk()
    root.title("Calificaciones Estudiantes")

    # Centrar la ventana en pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos = screen_width // 2 - 180
    y_pos = screen_height // 2 - 180
    root.geometry(f"+{x_pos}+{y_pos}")

    # Crear un marco para agrupar los elementos
    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20)
    frame.update()

    # Seleccionar Archivo de Entrada
    label_file_input = ctk.CTkLabel(frame, text="Seleccionar Archivo a Leer:")
    label_file_input.pack()
    button_file_input = ctk.CTkButton(frame, text="Examinar...", command = buscar_archivo_entrada)
    button_file_input.pack(pady=10)
    GB_FILE_PATH_INPUT = ctk.CTkEntry(frame, width=300)
    GB_FILE_PATH_INPUT.pack(padx=10, pady=20)

    # Definir Archivo de Salida
    label_file_output = ctk.CTkLabel(frame, text="Definir Archivo a Generar:")
    label_file_output.pack()
    button_file_output = ctk.CTkButton(frame, text="Guardar cómo...", command = definir_archivo_salida)
    button_file_output.pack(pady=10)
    GB_FILE_PATH_OUTPUT = ctk.CTkEntry(frame, width=300)
    GB_FILE_PATH_OUTPUT.pack(padx=10)

    # Procesamiento masivo de archivos
    button_process = ctk.CTkButton(frame, text="EJECUTAR \nPROCESO", command = ejecutar_proceso)
    button_process.pack(pady=40)
    
    # Iniciar bucle principal
    root.mainloop()