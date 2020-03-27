#libreria para trabajar la interfaz grafica de python
from tkinter import *
from tkinter.messagebox import *
#para instanciar
from functools import partial
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
#funciones para abrir y cerrar ventanas
def regresar(editarWin):
		editarWin.withdraw()
		inventario()

#funcion de la interfaz de inventario
def inventario():
	#cierra la ventana actual
	raiz.withdraw()
	#editarWin.withdraw()
	#inv es mi sig ventana
	inv=Tk()
	inv.title("INVENTARIO")
	inv.resizable(0,0)
	inv.geometry("640x480")

	labelEncabezado = Label(inv,text="INVENTARIO DE PRODUCTOS")
	labelEncabezado.grid(row=0,column=0,sticky="NW")
	labelEncabezado.place(x=250,y=10)
	labelProducto = Label(inv,text="aqui iran todos los producto que se registraron \nen al base de datos con sus respectivas caracteristicas")
	labelProducto.grid(row=0,column=0,sticky="NW")
	labelProducto.place(x=200,y=100)

	#este boton te redirigira a otra ventana
	Button(inv, text='AGREGAR PRODUCTOS', command=inv.destroy).place(x=100,y=300)
	#este boton te redirigira a otra ventana
	#ejemplo de como redirigirse a otra ventana con un botton
	#el codigo de aqui abajo
	Button(inv, text='EDITAR PRODUCTOS', command=partial(venEditar,inv)).place(x=250,y=300)
	#este boton te redirigira a otra ventana
	Button(inv, text='ELIMINAR PRODUCTOS', command=inv.destroy).place(x=400,y=300)
	
	
	
	
#pasando inv por parametros para poder cerrar la ventana
def venEditar(inv):
	#cerrando ventana actual
	inv.withdraw()

	#editarWin es mi sig ventana
	editarWin=Tk()
	editarWin.title("EDICION DE PRODUCTOS")
	editarWin.resizable(0,0)
	editarWin.geometry("640x480")
	labelEncabezado = Label(editarWin,text="EDICION DE PRODUCTOS")
	labelEncabezado.grid(row=0,column=0,sticky="NW")
	labelEncabezado.place(x=250,y=10)
	labelProducto = Label(editarWin,text="INGRESE CODIGO")
	labelProducto.grid(row=0,column=0,sticky="NW")
	labelProducto.place(x=200,y=100)
	cuadroCodigo=Entry(editarWin,text="c")
	cuadroCodigo.grid(row=1,column=0,sticky="NW")
	cuadroCodigo.place(x=250,y=100)
	#este boton te redirigira a otra ventana
	Button(editarWin, text='BUSCAR', command=editarWin.destroy).place(x=100,y=300)
	#este boton te redirigira a otra ventana
	#Button(inv, text='EDITAR PRODUCTOS', command=partial(venEditar,inv)).place(x=250,y=300)
	Button(editarWin, text='REGRESAR', command=partial(regresar,editarWin)).place(x=250,y=300)
	#este boton te redirigira a otra ventana
	
		
raiz.mainloop()
