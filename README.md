# Maestría Ciencia de Datos UNAJ

## Trabajo Final Integrador

## Nombre Asignatura: Programación

### Integrantes:
- Victor CONTI
- Deborah HERRERA
- Franco MANINI
- Julia FERNANDEZ

### Plazo de Entrega
El plazo de entrega del trabajo será de 30 días a partir de la última 
clase del curso (a dictarse el 29/4). Cumplido este plazo se podrá pedir prorroga, pero 
deberá hacerlo de manera explicita a los docentes del curso.

### Características del trabajo
El trabajo se realizará de forma grupal, en grupos de cuatro integrantes. El enunciado 
se tomará como base para los grupos que no tienen experiencia en programación. El 
tema de aplicación del trabajo se puede adaptar a las necesidades de cada grupo y 
aplicar a la profesión o ámbito laboral de cada estudiante.

### Características del informe
La  resolución  del  trabajo  (proyecto  de  dpython)  deberá  estar  acompañada  de  un 
informe que tendrá las siguientes características: 
- Introducción:  Breve descripción de la propuesta y de la interpretación de esta 
- Desarrollo:  Planificación  de  la  aplicación  que  deberá  ir  acompañada  de  un  
diagrama de flujo o seudocódigo que describa la lógica de funcionamiento del 
sistema. 
- Resultados: Mostrar los resultados obtenidos durante la ejecución de la 
aplicación comentando los pasos seguidos y agregando capturas que 
muestren dichos resultados. 
- Conclusiones:  Comentar  las  conclusiones  del  proyecto  y  sus  aportes  como 
actividad integradora.

### Descripción del Proyecto
Desarrollar un sistema de gestión académica que permita analizar las notas de los 
estudiantes  en  tres  asignaturas  diferentes.  Dicho  sistema  debería  poder  calcular  el  
promedio de notas, determinar la situación académica de cada estudiante (aprobado 
o reprobado), mostrar la información de los estudiantes, calcular el promedio general 
de todas las notas y el promedio de cada asignatura.

### Consignas del Proyecto  
1. Entrada de Datos desde Archivo CSV: 
Se debe leer las notas de tres asignaturas desde un archivo CSV. Este archivo 
contendrá los nombres de los estudiantes, incluyendo sus notas en 
matemáticas, ciencias y lenguaje. 
2. Cálculo del Promedio: 
Después de haber leído las notas desde el archivo CSV, calcular el promedio 
de las notas ingresadas para cada estudiante. Este promedio nos dará una idea 
general del rendimiento académico de cada estudiante en las tres asignaturas. Se requiere: 
-  Crear una función llamada “calcular_promedio”. 
-  Esta  función  debe  recibir  como  parámetro  la  lista  de  estudiantes 
obtenidos del inciso anterior. 
-  La función debe retornar en una lista el promedio de cada estudiante. 
3. Determinación de Situación Académica: 
Utilizar una estructura de control de flujo para determinar si cada estudiante 
aprueba  o  reprueba.  Si  el  promedio  de  las  notas  es  igual  o  mayor  a  6,  el  
estudiante aprobará, de lo contrario, reprobará. Se requiere: 
-  Crear una función llamada “determinar_situacion_academica”. 
-  Esta función debe recibir como parámetro la lista de promedios 
obtenidos del inciso anterior.
- La  función  debe  retornar  una  lista  de  “situaciones”  en  los  que  se  encuentra cada estudiante en base al promedio (aprobado o 
desaprobado).
4. Uso de Clases: 
Organizar el código utilizando en clases para modularizar la lógica. Definir una 
clase llamada Estudiante que tenga como mínimo los siguientes 
requerimientos: 
-  Atributos: nombre, nota_matematica, nota_ciencias y nota_lenguaje.  
-  Métodos: calcular el promedio y determinar la situación académica del estudiante.
5. Mostrar información:  
Se requiere almacenar los resultados en el archivo CSV y luego mostrar toda 
información  relevante  por  pantalla,  es  decir,  formar  mensajes  sencillos  para  
indicar la situación académica de cada estudiante: 
-  Nombre del estudiante 
-  Su promedio 
-  Su situación académica 
-  Concatenar solo los nombres de los estudiantes separados por comas 
(,). Ejemplo (salida esperada):  Nombres de los estudiantes: Francisco, Agustin, Mateo...
6. Como actividad extra se pide realizar Operaciones con Matrices: 
Utilizar NumPy u otras herramientas para realizar alguna operación adicional 
que involucre matrices. En el caso de utilizar Numpy no olvidarse de importar la librería con 
import numpy as np 
En este caso, se requiere: 
-  Obtener todas las notas como matrices con ‘np.array()’. 
-  Calcular el promedio general de todas las notas.
-  Calcular el promedio de cada asignatura en particular 
-  (Opcional) Calcular la desviación estándar de cada asignatura

### Ayuda
NumPy  proporciona  funciones  como  `np.mean()`  para  calcular  el  
promedio de los elementos de una matriz de manera más eficiente que con las 
listas de Python estándar. 


