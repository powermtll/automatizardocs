# Importamos librerías y métodos
import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

# Guardamos en nuestra variable doc nuestro documento
doc = DocxTemplate("plantilla.docx")

# Constantes del profesor

nombre_profesor = 'Daniel Sánchez Frontana'
tlf_profesor = '664706311'
correo_profesor= 'dsfrontana@gmail.com'
fecha = datetime.today().strftime("%d/%m/%Y")

# Creamos un diccionario con las constantes del profesor

constantes = {'nombre_profesor': nombre_profesor, 'tlf_profesor': tlf_profesor,
              'correo_profesor': correo_profesor, 'fecha': fecha}

# Nos traemos el dataframe con las notas mediante el excel
df = pd.read_excel('boletin_notas.xlsx')

for indice, fila in df.iterrows():
    contenido = {'nombre_estudiante':fila['Nombre Estudiante'],
                 'nota_matematicas':fila['Nota Matemáticas'],
                 'nota_ciencias':fila['Nota Ciencias'],
                 'nota_historia':fila['Nota Historia'],
                 'nota_ingles':fila['Nota Inglés'],
                 'nota_educacion_fisica':fila['Nota Educación Física'],
                 'curso':fila['Curso'],
                 'comentarios_matematicas':fila['Comentarios Matemáticas'],
                 'comentarios_ciencias':fila['Comentarios Ciencias'],
                 'comentarios_historia':fila['Comentarios Historia'],
                 'comentarios_ingles':fila['Comentarios Inglés'],
                 'comentarios_educacion_fisica':fila['Comentarios Educación Física']
                 }
    contenido.update(constantes)

    # Guardamos el valor del diccionario en el documento de word
    # Asignamos las variables
    doc.render(contenido)
    # Lo guardamos en un documento llamado prueba
    doc.save(f'notas_de_{fila["Nombre Estudiante"]}.docx')
    








































