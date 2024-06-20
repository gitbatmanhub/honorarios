import pandas as pd
import psycopg2
from datetime import datetime, timedelta
import requests
import base64

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname="samtest",
    user="postgres",
    password="Qtza5039",
    host="192.168.1.95",  
    port="5432"
)


fecha_actual = datetime.now()

# Restar un día
ayer = fecha_actual - timedelta(days=1)

# Formatear como solo fecha, sin tiempo
fecha_ayer = ayer.date()

fecha_formateada = fecha_ayer.strftime("%d-%m-%Y")


# Ejecutar la consulta
sql = '''select
    sus.cod_usuario as cod_medico,
    pmed.cli_nombres_completos name_medico,
    ode.cod_orden_servicio orden_servicio,
    ode.cod_orden_detalle orden_detalle,
    spe.cod_servicio_procedimiento id_servicio,
    spe.serv_nombre servicio,
    ode.lab_fecha_atendida :: date fecha_atencion,
    ac.fecha_inicia:: time hora_agenda,
    ode.lab_fecha_atendida :: time hora_atencion,
    pac.cod_sistema_externo hc,
    pac.cli_no_identificacion identificacion,
    pac.cli_nombres_completos names_paciente,
    es.sucursal_nombre_comercial as sucursal_atencion,
    en3.cli_razon_social empresa,
    case when en2.cod_tipo_comportamiento = 2 then en1.cli_razon_social else en2.cli_razon_social end convenio,
    ode.orden_convenio valor_seguro,
    ode.orden_copago,
    ode.convenio_ajuste,
    ode.orden_pvp

from demo.orden_detalles ode
         inner join demo.servicios_procedimientos spe on spe.cod_servicio_procedimiento = ode.cod_servicio_procedimiento
         inner join demo.ordenes_servicio ose on ose.cod_orden_servicio = ode.cod_orden_servicio
         inner join demo.personas_admisiones pam on pam.cod_persona_admision = ose.cod_persona_admision
         inner join demo.cli_empresas en3 on en3.cod_empresa = pam.cod_empresa_cliente
         inner join demo.cli_empresas en2 on en2.cod_empresa = en3.cod_empresa_principal
         left join demo.cli_empresas en1 on en1.cod_empresa = en2.cod_empresa_principal
         inner join demo.personas pac on pac.cod_persona = pam.cod_persona_paciente
         inner join demo.seg_usuarios sus on sus.cod_usuario = ode.cod_usuario
         inner join demo.personas pmed on pmed.cod_persona = sus.cod_persona
         inner join demo.empresas_sucursales es on es.cod_sucursal = ose.cod_sucursal
         left join demo.agenda_citas ac ON ac.cod_orden_detalle = ode.cod_orden_detalle
where date(ode.lab_fecha_atendida) between '2024-05-01' and '2024-05-02' and ord_origen not in ('FARMACIA') limit 10;'''
df = pd.read_sql(sql, conn)

# Guardar el DataFrame en un archivo Excel en la ruta especificada
ruta_archivo = r"C:\Users\Desarrollo\Desktop\"+str(fecha_formateada)+".xlsx"
df.to_excel(ruta_archivo, index=False)

conn.close()

# Leer el archivo en modo binario
with open(ruta_archivo, 'rb') as archivo:
    datos_binarios = archivo.read()

# Codificar los datos binarios en base64
datos_base64 = base64.b64encode(datos_binarios)

# Convertir a una cadena de caracteres para poder manipular o enviar como texto
cadena_base64 = datos_base64.decode('utf-8')
# Enviar reporte por Correo 
url = 'http://192.168.2.14:8089/api/send'
response = requests.get(url)
datos = {
  "destinatario": [
    "eromero@medilink.com.ec", "dcarrera@medilink.com.ec"
  ],
  "destinatarioCC": [],
  "asunto": "Producción Médicos",
  "body": "Reporte de producción médicos.",
  "adjunto": cadena_base64,
  "nombre_adjunto": "produccion_"+str(fecha_formateada)+".xlsx"
}


# Realizar la solicitud POST
response = requests.post(url, json=datos)

# Verificar la respuesta
if response.status_code == 200 or response.status_code == 201:
    print("Email enviado exitosamente")
    # Aquí puedes imprimir la respuesta JSON si la API devuelve algo relevante
    print(response.json())
else:
    print("Error al enviar el email:", response.status_code)
    # Es útil imprimir el cuerpo de la respuesta para entender el error
    print(response.text)