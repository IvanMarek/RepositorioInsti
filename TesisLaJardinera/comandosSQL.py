import sqlite3

base_datos = sqlite3.connect('LaJardinera.bd')
cursor = base_datos.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS producto(
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCAHR (255) NOT NULL,
    precio FLOAT NOT NULL,
    cantidad FlOAT NOT NULL,
    id_proveedor INT,
    id_categoria INT,
    imagen BLOB,
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)   
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS proveedor(
    id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
    razon_social VARCHAR (255) NOT NULL,
    cuit VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255),
    numero_telefono VARCHAR(255),
    email VARCHAR(255)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categoria(
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255)   
    )
''')
