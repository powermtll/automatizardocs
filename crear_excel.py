import pandas as pd

# Datos de ejemplo para los estudiantes
data = {
    "Nombre Estudiante": ["Juan Pérez", "María Gómez", "Luis Martínez", "Ana Torres"],
    "Curso": ["1º Bachillerato", "2º Bachillerato", "1º Bachillerato", "2º Bachillerato"],
    "Nota Matemáticas": [8.5, 9.0, 7.0, 6.5],
    "Comentarios Matemáticas": ["Muy bien", "Excelente", "Necesita mejorar", "Bien"],
    "Nota Ciencias": [7.0, 8.0, 6.5, 9.0],
    "Comentarios Ciencias": ["Bien", "Muy bien", "Regular", "Excelente"],
    "Nota Historia": [9.0, 7.5, 8.0, 8.5],
    "Comentarios Historia": ["Excelente", "Bien", "Muy bien", "Bien"],
    "Nota Inglés": [8.0, 7.0, 9.0, 6.0],
    "Comentarios Inglés": ["Bien", "Regular", "Excelente", "Necesita mejorar"],
    "Nota Educación Física": [9.5, 8.5, 9.0, 7.5],
    "Comentarios Educación Física": ["Muy bien", "Bien", "Excelente", "Bien"]
}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Guardar el DataFrame en un archivo de Excel (opcional)
df.to_excel("boletin_notas.xlsx", index=False)
