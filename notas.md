

# Temario VIM
## Comandos básicos
Esc: Salir de modo de edición
:wq!: Guardar y salir
:q!: Salir sin guardar
i: Entrar en modo de edición
ls: listar archivos
tab: recomendaciones

### Modos de Vim:
1. **Modo Normal (Modo de Comandos):**
   - `i`: Cambiar al modo de inserción (para empezar a escribir).
   - `ESC`: Salir del modo de inserción y volver al modo normal.
   - `dd`: Borrar la línea actual.
   - `yy`: Copiar la línea actual.
   - `p`: Pegar el contenido copiado o cortado después del cursor.
   - `u`: Deshacer la última acción.
   - `Ctrl + r`: Rehacer la última acción deshecha.

### Navegación y Edición:
2. **Modo de Inserción:**
   - `a`: Insertar texto después del cursor.
   - `A`: Insertar texto al final de la línea.
   - `o`: Abrir una nueva línea debajo de la línea actual e ingresar al modo de inserción.
   - `O`: Abrir una nueva línea encima de la línea actual e ingresar al modo de inserción.

3. **Modo Visual:**
   - `v`: Activar el modo visual para seleccionar texto.
   - `V`: Activar el modo visual para seleccionar líneas completas.

### Comandos de Búsqueda y Reemplazo:
4. **Buscar y Reemplazar:**
   - `/`: Iniciar búsqueda hacia adelante.
   - `?`: Iniciar búsqueda hacia atrás.
   - `n`: Ir a la siguiente coincidencia de búsqueda.
   - `N`: Ir a la anterior coincidencia de búsqueda.
   - `:%s/busqueda/reemplazo/g`: Reemplazar "busqueda" por "reemplazo" en todo el archivo.

### Otros Comandos Útiles:
5. **Guardar y Salir:**
   - `:w`: Guardar el archivo.
   - `:q`: Salir del editor (si no hay cambios sin guardar).
   - `:q!`: Salir del editor sin guardar cambios.
   - `:wq` o `ZZ`: Guardar y salir.

6. **Ayuda y Documentación:**
   - `:help comando`: Obtener ayuda sobre un comando específico.

### Personalización y Configuración:
7. **Configuración y Personalización:**
   - `~/.vimrc`: Archivo de configuración de Vim donde puedes definir atajos, opciones y plugins.

-------------------


# Temario git

## Comandos básicos

Comandos básicos de git 20/06/2024 by Edwin 

- Git commit -m "Mensaje del commit": Guarda los cambios en el repositorio local

- Git Push: Sube los cambios al repositorio remoto

- Git Pull: Descarga los cambios del repositorio remoto

- Git Clone "urlRepository": Clona un repositorio remoto en el repositorio local

-Git add . : seleccionar todos los cambios para el commit

# Encabezado de nivel 1
## Encabezado de nivel 2
### Encabezado de nivel 3

**Texto en negrita**
*Texto en cursiva*

- Elemento 1
- Elemento 2
  - Subelemento A
  - Subelemento B

1. Primer elemento
2. Segundo elemento

[Texto del enlace](URL)

![Texto alternativo](URL_de_la_imagen)

`Código inline`
```python
def ejemplo():
    print("Hola, mundo!")

Para bloques de código, se usa triple tilde invertido (\```) seguido opcionalmente del lenguaje de programación para resaltar la sintaxis.

> Este es un bloque de cita.

---
\*Texto sin formato\*

| Encabezado 1 | Encabezado 2 |
|--------------|--------------|
| Celda 1,1    | Celda 1,2    |
| Celda 2,1    | Celda 2,2    |

