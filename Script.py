import pandas as pd
import re  # Importar el módulo de expresiones regulares

# Paso 2: Crear un DataFrame de ejemplo
df = pd.read_excel('input_xlsx')

# Definir la lista de términos a buscar
terminos = []

# Definir una función que busque el primer término coincidente usando expresiones regulares
def buscar_primer_termino2(texto):
    # Crear una expresión regular que busca los términos como palabras completas
    regex_pattern = r'\b(' + '|'.join(terminos) + r')\b'
    match = re.search(regex_pattern, texto)
    return match.group(0) if match else None

# Paso 5: Aplicar la función para crear la nueva columna 'z'
df['z'] = df['x'].apply(buscar_primer_termino2)

# Paso 6: Mostrar el resultado
print(df)

df.to_excel('output_xlsx', index = False)
