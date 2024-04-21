###########
# MODULES #
###########

# Python
import pandas as pd


##########
# CLASES #
##########

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
        
#################
# GLOBAL VALUES #
#################

GB_FILE_PATH = "C:\\Users\\victo\\OneDrive\\Documents\\_ESTUDIOS\\0_UNAJ_DATA_SCIENCE\\UNAJ_MASTER_DATA_SCIENCE\\mi5502_Programación\\TFI\\notas_alumnos.csv"


########
# TEST #
########

if __name__ == "__main__":
    
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