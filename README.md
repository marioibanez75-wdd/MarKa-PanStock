# PanStock — Sistema de Control de Stock para Panadería

PanStock es una aplicación de escritorio desarrollada en Python para administrar el inventario de una panadería. Utiliza una base de datos MySQL para almacenar productos, categorías y movimientos de stock.

## Funcionalidades

- Gestión de productos.
- Gestión de categorías.
- Registro de movimientos de stock: entradas y salidas.
- Consulta del stock actual de cada producto.
- Control de stock mínimo para identificar productos con existencias bajas.
- Consultas y reportes, con filtros según las opciones implementadas en la aplicación.

## Tecnologías utilizadas

- **Python 3**
- **MySQL 8.0 o superior**
- **Tkinter**, para la interfaz gráfica.
- **MySQL Connector/Python**, para conectar Python con MySQL.
- **SQL**, para crear y administrar la base de datos.

## Requisitos previos

Antes de ejecutar el proyecto, instalá:

- Python 3.
- MySQL Server 8.0 o superior.
- El cliente de MySQL, si vas a importar la base de datos desde una terminal.

Asegurate de que el servicio de MySQL esté iniciado.

## 1. Importar la base de datos

Abrí una terminal en la carpeta donde se encuentra el archivo SQL y ejecutá:

```bash
mysql -u root -p < panstock.sql
```

Cuando MySQL solicite la contraseña, ingresá la contraseña del usuario `root`.

**Importante:** si el archivo se llama `panstock_implementacion.sql`, reemplazá `panstock.sql` por ese nombre en el comando. Usá el nombre del archivo que realmente esté incluido en el repositorio. Si el script no crea la base de datos `panstock`, creala antes de importar el archivo.

El script SQL puede incluir la estructura de las tablas, relaciones, restricciones, datos de prueba y configuración de usuarios y permisos, según el contenido de la versión utilizada.

## 2. Configurar la conexión a MySQL

Abrí `conexion.py` y verificá los parámetros de conexión:

- Host, normalmente `localhost`.
- Usuario de MySQL.
- Contraseña del usuario.
- Nombre de la base de datos: `panstock`.
- Puerto de MySQL, normalmente `3306`.

Si la aplicación se conecta con el usuario `panstock_app`, comprobá que ese usuario exista, que la contraseña coincida con la configurada en el código y que tenga los permisos necesarios sobre la base de datos.

Si el script SQL crea usuarios con contraseñas de ejemplo, cambiá esas contraseñas antes de usar el sistema fuera de un entorno de prueba. No publiques contraseñas reales en GitHub.

## 3. Instalar la dependencia de Python

Desde una terminal, ejecutá:

```bash
py -m pip install mysql-connector-python
```

Si el comando `py` no está disponible, probá:

```bash
python -m pip install mysql-connector-python
```

## 4. Verificar los archivos del proyecto

Comprobá que estén presentes los archivos necesarios:

- `menu.py`: inicia el menú o la interfaz principal.
- `conexion.py`: contiene la función de conexión a MySQL.
- `panstock_app.py`: debe estar presente si `menu.py` importa `PanStockApp` desde ese módulo.
- `panstock.sql` o `panstock_implementacion.sql`: contiene el script de la base de datos.

Si el código importa otros módulos de Python, esos archivos también deben estar disponibles en la carpeta del proyecto.

## 5. Ejecutar la aplicación

Desde la carpeta del proyecto, ejecutá:

```bash
py menu.py
```

Si tu instalación utiliza el comando `python`, podés ejecutar:

```bash
python menu.py
```

## 6. Estructura de la base de datos

La base de datos `panstock` utiliza las siguientes tablas principales:

- **`categorias`**: almacena las categorías de productos.
- **`productos`**: almacena la información de los productos.
- **`movimientos`**: registra las entradas y salidas de stock.

Las relaciones y restricciones definidas en el script SQL ayudan a mantener la integridad de los datos. El stock actual se obtiene a partir de los movimientos registrados, de acuerdo con la lógica implementada en el proyecto.

## 7. Solución de problemas frecuentes

### Error de conexión con MySQL

- Verificá que el servicio de MySQL esté iniciado.
- Comprobá el host y el puerto.
- Revisá el nombre de la base de datos, el usuario y la contraseña en `conexion.py`.

### Error `Access denied for user`

Verificá que el usuario indicado en `conexion.py` exista en MySQL, que la contraseña sea correcta y que tenga los permisos necesarios sobre la base de datos `panstock`. Crear la base de datos no crea automáticamente todos los usuarios que la aplicación pueda necesitar.

### Error relacionado con `panstock_app`

Si aparece un error al importar `PanStockApp`, comprobá que el archivo `panstock_app.py` esté en la carpeta del proyecto y que contenga la clase que `menu.py` intenta importar.

### Error al importar el archivo SQL

Verificá que la terminal esté ubicada en la carpeta correcta y que el nombre del archivo coincida exactamente con el utilizado en el comando. Si el script no crea la base de datos, asegurate de crearla antes de importar.

## Nota

Los nombres de archivos, parámetros de conexión, usuarios y permisos pueden variar según la versión del proyecto y la configuración local. Antes de entregar o ejecutar el sistema, verificá que los archivos incluidos en el repositorio coincidan con los indicados en estas instrucciones.
