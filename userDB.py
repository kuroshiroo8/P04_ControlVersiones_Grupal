import sqlite3

miConexion=sqlite3.connect("Usuarios")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE USUARIOS ( ID INTEGER PRIMARY KEY AUTOINCREMENT, USUARIO VARCHAR(50), CONTRASENA VARCHAR(50))")

variosUsuarios=[
	("Administrador", "password"),
	("Empleado", "password123")
]

# miCursor.execute("INSERT INTO USUARIOS VALUES("", "")")
#miCursor.executemany("INSERT INTO USUARIOS VALUES (NULL,?,?)", variosUsuarios)

miConexion.commit()

# Cerrar Conexion
miConexion.close()

# Solo se ejecuta CREATE TABLE 1 vez, si se desea anadir mas usuarios utilizar el primer instert