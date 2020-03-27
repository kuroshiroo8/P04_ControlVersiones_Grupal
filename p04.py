#libreria para trabajar la interfaz grafica de python
from tkinter import *
from tkinter.messagebox import *
import sqlite3

#raiz para la interfaz grafica de python
raiz=Tk()
raiz.title("Administrador de mermas")
raiz.resizable(0,0)
raiz.iconbitmap("covid-19.ico")
raiz.geometry("640x480")

#frame para la interfaz grafica de python para login
miFrame=Frame()
miFrame.pack()
miFrame.config(width="620", height="460")

#label de usuario para login
labelUser=Label(miFrame,text="Username:")
labelUser.grid(row=0,column=0,sticky="e", padx=10, pady=10)
#entry de usuario para login
cuadroUser=Entry(miFrame,text="User")
cuadroUser.grid(row=0,column=1, padx=10, pady=10)

#label de pass para login
labelPass=Label(miFrame,text="Password:")
labelPass.grid(row=1,column=0,sticky="e", padx=10, pady=10)
#entry de pass para login
cuadroPass=Entry(miFrame,text="Pass")
cuadroPass.grid(row=1,column=1, padx=10, pady=10)
cuadroPass.config(show="*")

def login():
 #Conectar con DB
 db = sqlite3.connect('Usuarios.db')
 c = db.cursor()

 usuario = cuadroUser.get()
 contra = cuadroPass.get()

 c.execute('SELECT * FROM USUARIOS WHERE USUARIO = ? AND CONTRASENA = ?', (usuario, contra))

 if c.fetchall():
 	#inventario es un funcion que manda a llamar la otra interfaz
 	inventario()
  #showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
 else:
  showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
   
 c.close()

#boton para login
#def codigoBoton():
Button (text="Login", command = login).pack()#command=codigoBoton
#funcion de la interfaz de inventario
def inventario():
	#cierra la ventana actual
	raiz.withdraw()
	#win es mi sig ventana
	inv=Tk()
	inv.title("INVENTARIO")
	inv.resizable(0,0)
	#raiz.iconbitmap("covid-19.ico")
	inv.geometry("640x480")

	
	#frame para la interfaz grafica de python para inventario
	miFrame=Frame()
	miFrame.pack()
	miFrame.config(width="620", height="460")
	labelEncabezado = Label(inv,text="INVENTARIO DE PRODUCTOS")
	labelEncabezado.grid(row=0,column=0,sticky="NW")
	labelEncabezado.place(x=250,y=10)

	labelProducto = Label(inv,text="aqui iran todos los producto que se registraron \nen al base de datos con sus respectivas caracteristicas")
	labelProducto.grid(row=0,column=0,sticky="NW")
	labelProducto.place(x=200,y=100)

	#este boton te redirigira a otra ventana
	Button(inv, text='AGREGAR PRODUCTOS', command=inv.destroy).place(x=100,y=300)
	#este boton te redirigira a otra ventana
	Button(inv, text='EDITAR PRODUCTOS', command=inv.destroy).place(x=250,y=300)
	#este boton te redirigira a otra ventana
	Button(inv, text='ELIMINAR PRODUCTOS', command=inv.destroy).place(x=400,y=300)
	#ejemplo de como redirigirse a otra ventana con un botton
	#el codigo de aqui abajo
	#Button(ventana, text='AGREGAR PRODUCTOS', command=abrirventana).place(x=270,y=150)


raiz.mainloop()

