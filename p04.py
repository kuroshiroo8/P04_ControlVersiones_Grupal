#libreria para trabajar la interfaz grafica de python
import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.messagebox import *

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
 	#Principal es un funcion que manda a llamar la otra interfaz
 	principal()
  #showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
 else:
  showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
   
 c.close()

#boton para login
#def codigoBoton():
Button (text="Login", command = login).pack()#command=codigoBoton



#Funcion Agregar Poductos
def venAgregarP(inv):	
	inv.withdraw()
	agregarWin=Tk()
	agregarWin.title("REGISTRAR PRODUCTOS")
	agregarWin.resizable(0,0)
	agregarWin.geometry("640x480")
	#label de encabezado
	labelEncabezado = Label(agregarWin,text="REGISTRO DE PRODUCTOS")
	labelEncabezado.grid(row=0,column=0,sticky="NW")
	labelEncabezado.place(x=250,y=10)
	#label de usuario para Producto
	labelCodigo=Label(agregarWin,text="Codigo:")
	labelCodigo.grid(row=0,column=0,sticky="e",padx=20, pady=100)
	cuadroCodigo=Entry(agregarWin,textvariable="Code")
	cuadroCodigo.grid(row=0,column=1, sticky="e",padx=20, pady=100)

	#label de usuario para Precio
	labelNombre=Label(agregarWin,text="Nombre:")
	labelNombre.grid(row=0,column=2,sticky="e",padx=1, pady=5)
	cuadroNombre=Entry(agregarWin,textvariable="User")
	cuadroNombre.grid(row=0,column=3, sticky="e",padx=30, pady=5)

	#label de usuario para cantidad
	labelCantidad=Label(agregarWin,text="Cantidad:")
	labelCantidad.grid(row=1,column=0,sticky="e",padx=15, pady=5)
	cuadroCantidad=Entry(agregarWin,textvariable="Cant")
	cuadroCantidad.grid(row=1,column=1, sticky="e",padx=15, pady=5)

	#label de usuario para Codigo
	labelPrecio=Label(agregarWin,text="Precio:")
	labelPrecio.grid(row=1,column=2,sticky="e",padx=20, pady=5)
	cuadroPrecio=Entry(agregarWin,textvariable="Costo")
	cuadroPrecio.grid(row=1,column=3, sticky="e",padx=15, pady=5)

	Button(agregarWin, text='AGREGAR', command=agregarWin.destroy).place(x=150,y=300)
	
	Button(agregarWin, text='REGRESAR', command=partial(regresar,agregarWin)).place(x=350,y=300)

########################interfaz para ver los productos
def venMostrar():
    #windows.withdraw()
    MostrarWin=tk.Toplevel()
    MostrarWin.geometry("640x480")
    e1=tk.Label(MostrarWin, text="VER PRODUCTOS :",bg="white",fg="black").place(x=50, y=50),
    lbl_code=tk.Label(MostrarWin, text="CODIGO",bg="white",fg="black").place(x=50, y=70)
    lbl_name=tk.Label(MostrarWin, text="NOMBRE",bg="white",fg="black").place(x=110, y=70)
    lbl_cant=tk.Label(MostrarWin, text="CANTIDAD",bg="white",fg="black").place(x=180, y=70)
    lbl_prec=tk.Label(MostrarWin, text="PRECIO",bg="white",fg="black").place(x=260, y=70)

  ###########consulta para mostrar los productos de la base
    def mostrar():
##        codigo
        lista=tk.Listbox(MostrarWin, width = 50, font=("arial", 12), height =15 )
        lista.pack()
        db = sqlite3.connect("articulos.db")
        c = db.cursor()
        c.execute( "select *from articulos  ORDER BY (ID)DESC" )
        for row in c:
            lista.insert(0,str(row[1])+" --------"+ row[2]+"--------"+ str(row[3])+"--------"+ str(row[4]))
            lista.place(x=50,y=90)


    menu=tk.Button(MostrarWin, text="MENU", fg="red",command = MostrarWin.destroy)
    menu.pack()
    menu.place(x=50,y=400)

    bt_mostrar = tk.Button(MostrarWin, text =  "MOSTRAR PRODUCTOS", fg="green",command = mostrar)
    bt_mostrar.pack()
    bt_mostrar.place(x=280,y=400)



def venBorrarP(inv):
	inv.withdraw()
	borrarWin=Tk()
	borrarWin.title("ELIMINAR PRODUCTOS")
	borrarWin.resizable(0,0)
	borrarWin.geometry("640x480")
	raiz.config(backgroun="grey",padx=15, pady=80)
	labelEncabezado = Label(borrarWin,text="ELIMINAR PRODUCTO")
	labelEncabezado.grid(row=0,column=0,sticky="NW")
	labelEncabezado.place(x=250,y=10)

	labelEliminar=Label(borrarWin,text="Codigo Del Producto:")
	labelEliminar.grid(row=0,column=0,sticky="e",padx=80, pady=150)
	cuadroEliminar=Entry(borrarWin,text="Code")
	cuadroEliminar.grid(row=0,column=1, sticky="e",padx=30, pady=160)

	Button(borrarWin, text='ELIMINAR', command=borrarWin.destroy).place(x=210,y=300)
	
	Button(borrarWin, text='REGRESAR', command=partial(regresar,borrarWin)).place(x=290,y=300)
    #interfaz para modificar el productos
  
 ###################### VENTANA PARA MODIFICAR

def venEditar():
    #windows.withdraw()
    editarWin=tk.Toplevel()
    editarWin.title("MODIFICAR")
    editarWin.resizable(0,0)
   
    editarWin.geometry("640x480")
    lbl_Encabezado=tk.Label(editarWin, text=" MODIFICAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=50)
    
#texbox para id
    
    ProctID=tk.StringVar()
    cuadroID=tk.Entry(editarWin,textvariable=ProctID).place(x=50, y=120)

#textbox para codigo

    lblcode=tk.Label(editarWin, text="INGRESE CODIGO DEL PRODUCTO", padx=10 ).place(x=30, y=100)

#txtxbox para nombre
    Proctname=tk.StringVar()
    cuadroVx=tk.Entry(editarWin,textvariable=Proctname).place(x=50, y=170)
#textbox para la cantidad
    
    Proctncand=tk.StringVar()
    cuadroVx=tk.Entry(editarWin,textvariable=Proctncand).place(x=50, y=230)

#textbo para el precio
    
    Proctnprec=tk.StringVar()
    cuadroVx=tk.Entry(editarWin,textvariable=Proctnprec).place(x=50, y=280)
###############################################################

    #labels para los valores a modificar

    lblname=tk.Label(editarWin, text="INGRESE EL NUEVO NOMBRE PARA EL PRODUCTO", padx=10 ).place(x=30, y=150)
    lblcant=tk.Label(editarWin, text="INGRESE EL NUEVO CANTIDAD PARA EL PRODUCTO", padx=10 ).place(x=30, y=200)
    lblprec=tk.Label(editarWin, text="INGRESE EL NUEVO PRECIO PARA EL PRODUCTO", padx=10 ).place(x=30, y=250)
    
  ################modificar el producto consulta
    def modificar():
        db = sqlite3.connect("articulos.db")
        c = db.cursor()

        id_producto = ProctID.get()
        nuevo_no = Proctname.get()
        nuevo_ca = Proctncand.get()
        nuevo_pr = Proctnprec.get()
    
        c.execute("update articulos set (nombre,cantidad,precio) =('"+nuevo_no+"','"+nuevo_ca+"','"+nuevo_pr+"') where codigo = ('"+id_producto+"')")
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACION","ARTICULO MODIFICADO" )
        editarWin.destroy()
        venEditar()

#### BOTON PARA MENU
    
    menu=tk.Button(editarWin, text="MENU", fg="red",command = editarWin.destroy)
    menu.pack()
    menu.place(x=50,y=350)
#### BOTON PARA MODIFICAR
    bt_modificar = tk.Button(editarWin, text =  "MODIFICAR PRODUCTO", fg="green",command = modificar)
    bt_modificar.pack()
    bt_modificar.place(x=280,y=350)



###################funcion de la interfaz de inventario
def principal():
	#cierra la ventana actual
	raiz.withdraw()
	#editarWin.withdraw()
	#inv es mi sig ventana
	inv=tk.Toplevel()
	inv.title("INVENTARIO")
	inv.resizable(0,0)
	inv.geometry("640x480")

	lbl_Encabezado = Label(inv,text="INVENTARIO DE PRODUCTOS")
	lbl_Encabezado.grid(row=0,column=0,sticky="NW")
	lbl_Encabezado.place(x=250,y=10)
	#boton para dirigirse a la interfaz de agregar producto
	bt_add=tk.Button(inv,text="Agregar Producto", command = inv.destroy)
	bt_add.pack()
	bt_add.place(x=5,y=50)
	#boton para dirigirse a la interfaz de mostrar producto
	bt_view=tk.Button(inv,text="Mostrar Productos", command = venMostrar)
	bt_view.pack()
	bt_view.place(x=5,y=150)
	#boton para dirigirse a la interfaz de eliminar producto
	bt_delet=tk.Button(inv,text="Eliminar Producto",  command = inv.destroy)
	bt_delet.pack()
	bt_delet.place(x=5,y=250)
	#boton para dirigirse a la interfaz de modificar producto
	bt_edit=tk.Button(inv,text="Modificar Producto",  command = venEditar)
	bt_edit.pack()
	bt_edit.place(x=5,y=350)
		
raiz.mainloop()
