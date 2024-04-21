###########
# MODULES #
###########

# Python
import os
from tkinter import filedialog

# Third-Party
import customtkinter as ctk

# Project
from utils import ImportarDesdeArchivo, Estudiante

#############
# FUNCTIONS #
#############

def ejecutar_proceso():
    global GB_FILE_PATH

    # Importamos los datos generales de los estudiantes desde el archivo csv
    datos = ImportarDesdeArchivo(GB_FILE_PATH)
    df_datos = datos.getDatos()
    
    # Mostramos en consola los datos importados
    print()
    print("DATOS GENERALES IMPORTADOS DE LOS ESTUDIANTES:")
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
        print(f"ESTUDIANTE n°{index + 1}")
        print(f"    > {estudiante}")
        print(f"    > Promedio: {promedio:.2f}")
        print(f"    > Situación Académica: {situacion_academica}")
        print()
        
        # Actualizamos los datos generales de los estudiantes
        # Agregamos el promedio y la situación académica      
        df_datos.loc[index, "Promedio"] = round(promedio, 2)
        df_datos.loc[index, "Situacion_Academica"] = situacion_academica
    
    print("DATOS GENERALES ACTUALIZADOS DE LOS ESTUDIANTES:")
    print(df_datos)
    print()

def buscar_archivo():
    global GB_FILE_PATH
    file_path = filedialog.askopenfilename()
    GB_FILE_PATH.delete(0, ctk.END)
    GB_FILE_PATH.insert(0, file_path)
    print("**********")
    print(GB_FILE_PATH.get())
    print("**********")


#################
# GLOBAL VALUES #
#################

GB_FILE_PATH = ""


########
# MAIN #
########
    
if __name__ == "__main__":
    
    # Crear la ventana de la interfaz gráfica
    root = ctk.CTk()
    root.title("Sistema de Gestión Estudiantes")
    # root.iconbitmap("bionexo_0.ico")

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

    # Seleccionar Archivo
    label_file = ctk.CTkLabel(frame, text="Seleccionar Archivo:")
    label_file.pack()
    button_file = ctk.CTkButton(frame, text="Examinar...", command = buscar_archivo)
    button_file.pack(pady=10)
    GB_FILE_PATH = ctk.CTkEntry(frame, width=300)
    GB_FILE_PATH.pack(padx=10)


    # Procesamiento masivo de archivos
    button_process = ctk.CTkButton(frame, text="EJECUTAR \nPROCESO", command = ejecutar_proceso)
    button_process.pack(pady=10)
    
    # Iniciar bucle principal
    root.mainloop()