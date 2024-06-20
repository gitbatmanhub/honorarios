import pandas as pd
import warnings

# Suprimir advertencias específicas de openpyxl
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Ruta al archivo Excel
archivo_excel = './excelHonorarios/honorarios.xlsx'
hoja = 'PRODUCCION' 
columnas_por_nombre = ['medico', 'sucursal_nombre_comercial', 'CONCEOTO', 'servicio', 'hora_atencion', 'fecha_atencion']

try:
    # Leer la hoja especificada del archivo Excel
    data = pd.read_excel(archivo_excel, sheet_name=hoja)
    
    # Leer columnas específicas por nombre
    data_columnas_por_nombre = data[columnas_por_nombre]
    
    # Convertir el DataFrame a JSON y almacenar en una variable
    resultados_json = data_columnas_por_nombre.to_json(orient='records', lines=True)
    
    print("Columnas leídas por nombre:")
    print(data_columnas_por_nombre.head())
    
    # Imprimir los resultados almacenados en la variable JSON (opcional)
    print("\nResultados JSON:")
    print(resultados_json)

except FileNotFoundError:
    print(f"El archivo {archivo_excel} no fue encontrado.")
except KeyError as e:
    print(f"Una de las columnas especificadas no existe: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
