import sqlite3

# 1. Establecemos la conexión (Establece el enlace lógico (crea el archivo si la ruta carece de él))
conexion = sqlite3.connect("biblioteca.db")

# 2. Instanciamos el Cursor para procesar sentencias SQL hacia el motor
cursor = conexion.cursor()

# 3. Le damos al cursor una sentencia SQL para ejecutar
# Usamos IF NOT EXISTS para que, si ejecutas esta celda dos veces, no dé un error.
# AUTOINCREMENT hace que la base de datos asigne el ID 1, 2, 3... automáticamente a cada registro.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        anio INTEGER
    )
""")

# 4. Las transacciones de alteración de esquema (DDL) como CREATE normalmente incurren en comprobación automática, pero garantizamos el flujo confirmando,
# pero es buena práctica sellar la transacción al final.
conexion.commit()
print("Esquema matricial 'libros' validado y operante exitosamente.")

titulo_nuevo = "1984"
autor_nuevo = "George Orwell"
anio_nuevo = 1949

# Sentencia SQL fija con "huecos" parametrizados (?)
sentencia = "INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)"
datos_empaquetados = (titulo_nuevo, autor_nuevo, anio_nuevo) # Obligatoriamente en Tupla

cursor.execute(sentencia, datos_empaquetados)

# ¡VITAL! Si no hacemos commit, este nuevo libro no persistirá físicamente en la unidad de almacenamiento general.
conexion.commit()
print("Libro procesado de forma segura y guardado permanentemente.")

# Procedemos a poblar datos auxiliares controlados para ejemplificar los conjuntos de operadores subsiguientes
cursor.execute(sentencia, ("Dune", "Frank Herbert", 1965))
cursor.execute(sentencia, ("Fundación", "Isaac Asimov", 1951))
cursor.execute(sentencia, ("El Quijote", "Miguel de Cervantes", 1605))
conexion.commit()

print("--- TODOS LOS LIBROS (SIN RESTRICCIONES PONDERADAS) ---")
cursor.execute("SELECT * FROM libros")
todos = cursor.fetchall()
for libro in todos:
    print(f"[{libro[0]}] {libro[1]}")

print("\n--- WHERE MATEMÁTICO: Libros del Registros Acotados desde la Década de 1900 ---")
# Busca libros que se hayan publicado a partir del año 1900 adelante.
cursor.execute("SELECT titulo, anio FROM libros WHERE anio >= 1900")
libros_modernos = cursor.fetchall()
for libro in libros_modernos:
    print(f"-> {libro[0]} ({libro[1]})")

print("\n--- WHERE POR EVALUACIÓN DE PATRÓN LÓGICO: Textos que empiecen por F ---")
# LIKE seguido de F y un %. Esto significa "Empieza por F estricto y luego admite cadenas de extensión indefinida ulteriores".
cursor.execute("SELECT titulo, autor FROM libros WHERE titulo LIKE 'F%'")
libros_f = cursor.fetchall()
for libro in libros_f:
    print(f"-> {libro[0]} de {libro[1]}")

print("\n--- MULTIPLES WHERE: AND y OR ---")
cursor.execute("SELECT titulo FROM libros WHERE anio < 1960 AND autor = 'Isaac Asimov'")
libros_clasicos_asimov = cursor.fetchall()
for libro in libros_clasicos_asimov:
    print(f"-> Conjunto cruzado: {libro[0]}") 

# Procedemos a actualizar el año de publicación del registro correspondiente a 'Dune'.
nuevo_anio = 2021
id_objetivo = 2

# Aplicamos la modificación de forma restrictiva y parametrizada utilizando la clave primaria.
cursor.execute("UPDATE libros SET anio = ? WHERE id = ?", (nuevo_anio, id_objetivo))

# Consolidamos la transacción en la base de datos.
conexion.commit()

print(f"Registro con ID {id_objetivo} actualizado correctamente.")

# Procedemos a eliminar un registro específico del sistema.
id_borrar = 4

# Instrucción de borrado que emplea la parametrización para garantizar una supresión unívoca.
cursor.execute("DELETE FROM libros WHERE id = ?", (id_borrar,))

# Consolidamos los cambios para hacer el borrado persistente.
conexion.commit()

print(f"Registro con ID {id_borrar} eliminado exitosamente de la base de datos.")


# 1. Creamos matriz física nueva de Usuarios con clave primaria estructurada con autoincremento garantizado
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
    )
""")

# 2. Creamos tabla intercesora temporal de Alquileres diseñada para articular esquemas Muchos-A-Muchos (M:N)
# Declaramos textualmente que el entero id_usuario NO es valor escalar exento... ES en realidad una Llave Foránea atada a usuarios(id) original.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alquileres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_libro INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
        FOREIGN KEY (id_libro) REFERENCES libros(id)
    )
""")

# 3. Insertamos y instanciamos e insertamos a un único usuario para alquilar el material atándolo por IDs.
cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Paco')")
cursor.execute("INSERT INTO alquileres (id_usuario, id_libro) VALUES (1, 1)") # El Usuario Paco (ID 1) solicita en préstamo vinculante y excluyente hacia 1984 (ID 1).
conexion.commit()

# 4. VISTA DE RESULTANTE EXTRAPOLADOR DE DATOS: IMPLEMENTACIÓN DE COMANDO JOIN
# Ejecutamos la consulta, concatenando las correlaciones PK/FK desde las tres vertientes uniendo de tal manera descripciones alfabéticas consolidadas.
consulta_join = """
    SELECT usuarios.nombre, libros.titulo
    FROM alquileres
    JOIN usuarios ON alquileres.id_usuario = usuarios.id
    JOIN libros ON alquileres.id_libro = libros.id
"""
cursor.execute(consulta_join)
prestamos = cursor.fetchall()

print("\n--- FORMATO DE SALIDA ESTANDARIZADA DE EXPEDIENTES Y REFERENCIAS (JOIN) ---")
for pr in prestamos:
    print(f"Alentamos al cobro del usuario '{pr[0]}' porque mantiene registro del ejemplar formal: '{pr[1]}'.")

# Cerramos formalmente nuestra conexión al final de la jornada completa de trabajo para liberar la memoria global.
conexion.close()
print("\nFlujo de la base de datos cerrado armónicamente.")

import sqlite3

# 1. Definimos una Clase que representa exactamente una fila de nuestra tabla 'libros'
class Libro:
    def __init__(self, id_libro, titulo, autor, anio):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"📖 {self.titulo} (escrito por {self.autor} en {self.anio})"

# 2. Nos conectamos, leemos los datos crudos y los transformamos en Objetos
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM libros")
datos_crudos = cursor.fetchall()
conexion.close()

# 3. El Mapeo (Mapping)
inventario_objetos = []
for fila in datos_crudos:
    # Desempaquetamos la tupla y creamos una instancia dinámica de Libro
    nuevo_objeto = Libro(fila[0], fila[1], fila[2], fila[3])
    inventario_objetos.append(nuevo_objeto)

# 4. Ahora trabajamos con Objetos puros de Python, mucho más limpios y seguros
print("--- INVENTARIO CARGADO EN OBJETOS ---")
for obj_libro in inventario_objetos:
    # Fíjate qué elegante es acceder a sus propiedades con el 'punto'
    if obj_libro.anio > 1950:
        print(f"Obra moderna: {obj_libro.titulo}")

    # Usamos su método mágico __str__
    print(obj_libro)
    print("-" * 20)