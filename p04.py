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
def venRegistrar():
    #windows.withdraw()
 
    RegistrarWin=tk.Toplevel()
    RegistrarWin.title("REGISTRAR")
    RegistrarWin.resizable(0,0)
    RegistrarWin.iconbitmap("13.ico")
    RegistrarWin.geometry("550x550")

    e1=tk.Label(RegistrarWin, text="AGREGAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=20)
 
# variable codigo
    entrycodigo=tk.StringVar()
    codigotx=tk.Entry(RegistrarWin,textvariable=entrycodigo).place(x=40, y=120)
   
# variable producto
    entryproducto=tk.StringVar()
    productotx=tk.Entry(RegistrarWin,textvariable=entryproducto).place(x=40, y=170)
    
# variable cantidad
    entrycantidad=tk.StringVar()
    cantidadtx=tk.Entry(RegistrarWin,textvariable=entrycantidad).place(x=40, y=220)

# variable  precio
    entryprecio=tk.StringVar()
    preciotx=tk.Entry(RegistrarWin,textvariable=  entryprecio).place(x=40, y=270)
    
# Etiqueta para "INGRESE CODIGO DEL PRODUCTO"
    etiquetacodigo=tk.Label(RegistrarWin, text="INGRESE CODIGO DEL PRODUCTO.", padx=10 ).place(x=30, y=100)
    
# Etiqueta para "INGRESE NOMBRE DEL PRODUCTO"
    etiquetanombre=tk.Label(RegistrarWin, text="INGRESE NOMBRE DEL PRODUCTO.", padx=10 ).place(x=30, y=150)

# Etiqueta para "INGRESE NOMBRE DEL CANTIDAD"
    etiquetacantidad=tk.Label(RegistrarWin, text="INGRESE CANTIDAD DEL PRODUCTO.", padx=10 ).place(x=30, y=200)
   

#Etiqueta para "INGRESE PRECIO DEL PRODUCTO"
    etiquetaprecio = tk.Label(RegistrarWin, text="INGRESE PRECIO DEL PRODUCTO", padx=10 ).place(x=30, y=250)

   ## Boton menu  

    menu=tk.Button(RegistrarWin, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = RegistrarWin.destroy)
    menu.pack()
    menu.place(x=50,y=350)

    def guarda():

            db = sqlite3.connect("articulos.db")
            c = db.cursor()

            codigo = entrycodigo.get()
            nombre = entryproducto.get()
            cantidad = entrycantidad.get()
            precio = entryprecio.get()
          

            c.execute("insert into articulos (codigo,nombre,cantidad,precio) values ('"+codigo+"','"+nombre+"','"+cantidad+"','"+precio+"')")
            db.commit()
            c.close()
            messagebox.showinfo("MODIFICACION","ARTICULO INGRESADO" )
            RegistrarWin.destroy()
            venRegistrar()

    btguardar = tk.Button(RegistrarWin, text =  "GUARDAR", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = guarda)
    btguardar.pack()
    btguardar.place(x=300,y=350)

########################interfaz para ver los productos
def venMostrar():
    #windows.withdraw()
    MostrarWin=tk.Toplevel()
    MostrarWin.geometry("640x480")
    e1=tk.Label(MostrarWin, text="VER PRODUCTOS :",bg="white",fg="black").place(x=50, y=50),
    lbl_code=tk.Label(MostrarWin, text="CODIGO",bg="white",fg="black").place(x=50, y=70)
    lbl_name=tk.Label(MostrarWin, text="NOMBRE",bg="white",fg="black").place(x=150, y=70)
    lbl_cant=tk.Label(MostrarWin, text="CANTIDAD",bg="white",fg="black").place(x=250, y=70)
    lbl_prec=tk.Label(MostrarWin, text="PRECIO",bg="white",fg="black").place(x=350, y=70)

  ###########consulta para mostrar los productos de la base
    def mostrar():
##        codigo
        lista=tk.Listbox(MostrarWin, width = 11, font=("arial", 12), height =15 )
        lista.pack()
        lista_3=tk.Listbox(MostrarWin, width = 5, font=("arial", 12), height =15 )
        lista_3.pack()
        lista_2=tk.Listbox(MostrarWin, width = 11, font=("arial", 12), height =15 )
        lista_2.pack()
       	lista_1=tk.Listbox(MostrarWin, width = 11, font=("arial", 12), height =15 )
        lista_1.pack()
        db = sqlite3.connect("articulos.db")
        c = db.cursor()
        c.execute( "select  *from articulos  ORDER BY (ID)DESC" )
        for row in c:
           lista.insert(0,row[2])
           lista.place(x=150,y=90)
           lista_1.insert(0,row[1])
           lista_1.place(x=50,y=90)
           lista_2.insert(0,str(row[3]))
       	   lista_2.place(x=250,y=90)
       	   lista_3.insert(0,str(row[4]))
           lista_3.place(x=350,y=90)


    menu=tk.Button(MostrarWin, text="MENU", fg="red",command = MostrarWin.destroy)
    menu.pack()
    menu.place(x=50,y=400)

    bt_mostrar = tk.Button(MostrarWin, text =  "MOSTRAR PRODUCTOS", fg="green",command = mostrar)
    bt_mostrar.pack()
    bt_mostrar.place(x=280,y=400)



def venBorrar():
    EliminarWin=tk.Toplevel()
    EliminarWin.title("ELIMINAR")
    EliminarWin.resizable(0,0)
    EliminarWin.iconbitmap("14.ico")
    EliminarWin.geometry("512x512")
    e1=tk.Label(EliminarWin, text=" ELIMINAR PRODUCTOS :",bg="white",fg="black").place(x=50, y=50)
    
#### VARIABLE PARA ID
    
    entry_id=tk.StringVar()
    productotx=tk.Entry(EliminarWin,textvariable=entry_id).place(x=50, y=150)

#### ETIQUETA PARA ID

    etiquetanombre=tk.Label(EliminarWin, text="INGRESE CODIGO DEL PRODUCTO", padx=10 ).place(x=30, y=115)
#
    def eliminar():
        db = sqlite3.connect("articulos.db")
        c = db.cursor()

        
        id_producto = entry_id.get()
        c.execute("DELETE  from articulos where codigo = ('"+id_producto+"')")
        messagebox.showinfo("MODIFICACION","ARTICULO ELIMINADO" )

        db.commit()
        c.close()
        EliminarWin.destroy()
        venBorrar()
        
#### BOTON PARA MENU
    
    menu=tk.Button(EliminarWin, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = EliminarWin.destroy)
    menu.pack()
    menu.place(x=50,y=350)
#### BOTON PARA ELIMINAR
    bt_eliminar = tk.Button(EliminarWin, text =  "ELIMINAR PRODUCTOS", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = eliminar)
    bt_eliminar.pack()
    bt_eliminar.place(x=280,y=350)
     
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


########################interfaz para ver agregar mermas
#Funcion Agregar Mermas
def venRegistrarM():
    #windows.withdraw()
 
    RegistrarWinM=tk.Toplevel()
    RegistrarWinM.title("RegistrarWinM")
    RegistrarWinM.resizable(0,0)
    RegistrarWinM.iconbitmap("13.ico")
    RegistrarWinM.geometry("550x550")

    e1=tk.Label(RegistrarWinM, text="AGREGAR MERMAS :",bg="white",fg="black").place(x=50, y=20)
 
# variable codigo
    entrycodigo=tk.StringVar()
    codigotx=tk.Entry(RegistrarWinM,textvariable=entrycodigo).place(x=40, y=120)
   
# variable producto
    entryproducto=tk.StringVar()
    productotx=tk.Entry(RegistrarWinM,textvariable=entryproducto).place(x=40, y=170)
    
# variable cantidad
    entrycantidad=tk.StringVar()
    cantidadtx=tk.Entry(RegistrarWinM,textvariable=entrycantidad).place(x=40, y=220)
    
# Etiqueta para "INGRESE CODIGO DEL PRODUCTO"
    etiquetacodigo=tk.Label(RegistrarWinM, text="INGRESE CODIGO DE MERMA.", padx=10 ).place(x=30, y=100)
    
# Etiqueta para "INGRESE NOMBRE DEL PRODUCTO"
    etiquetanombre=tk.Label(RegistrarWinM, text="INGRESE NOMBRE DE MARMA.", padx=10 ).place(x=30, y=150)

# Etiqueta para "INGRESE NOMBRE DEL CANTIDAD"
    etiquetacantidad=tk.Label(RegistrarWinM, text="INGRESE CANTIDAD DE MERMA.", padx=10 ).place(x=30, y=200)
   

   ## Boton menu  

    menu=tk.Button(RegistrarWinM, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = RegistrarWinM.destroy)
    menu.pack()
    menu.place(x=50,y=350)

    def guardaM():

            db = sqlite3.connect("articulos.db")
            c = db.cursor()

            codigo = entrycodigo.get()
            nombre = entryproducto.get()
            cantidad = entrycantidad.get()
          

            c.execute("insert into tbMerma (codigo,nombre,cantidad) values ('"+codigo+"','"+nombre+"','"+cantidad+"')")
            db.commit()
            c.close()
            messagebox.showinfo("MODIFICACION","MERMA INGRESADA" )
            RegistrarWinM.destroy()
            venRegistrarM()

    btguardar = tk.Button(RegistrarWinM, text =  "GUARDAR", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = guardaM)
    btguardar.pack()
    btguardar.place(x=300,y=350)    


########################interfaz para ver las mermas
def venMostrarM():
    #windows.withdraw()
    MostrarWinM=tk.Toplevel()
    MostrarWinM.geometry("640x480")
    e1=tk.Label(MostrarWinM, text="VER MERMAS :",bg="white",fg="black").place(x=50, y=50),
    lbl_code=tk.Label(MostrarWinM, text="CODIGO",bg="white",fg="black").place(x=50, y=70)
    lbl_name=tk.Label(MostrarWinM, text="NOMBRE",bg="white",fg="black").place(x=110, y=70)
    lbl_cant=tk.Label(MostrarWinM, text="CANTIDAD",bg="white",fg="black").place(x=180, y=70)

  ###########consulta para mostrar los productos de la base
    def mostrarM():
##        codigo
        lista=tk.Listbox(MostrarWinM, width = 50, font=("arial", 12), height =15 )
        lista.pack()
        db = sqlite3.connect("articulos.db")
        c = db.cursor()
        c.execute( "select *from tbMerma  ORDER BY (ID)DESC" )
        for row in c:
            lista.insert(0,str(row[1])+" --------"+ row[2]+"--------"+ str(row[3]))
            lista.place(x=50,y=90)


    menu=tk.Button(MostrarWinM, text="MENU", fg="red",command = MostrarWinM.destroy)
    menu.pack()
    menu.place(x=50,y=400)

    bt_mostrar = tk.Button(MostrarWinM, text =  "MOSTRAR MERMAS", fg="green",command = mostrarM)
    bt_mostrar.pack()
    bt_mostrar.place(x=280,y=400)

#####################################################################################################################

def venBorrarM():
    EliminarWinM=tk.Toplevel()
    EliminarWinM.title("ELIMINAR")
    EliminarWinM.resizable(0,0)
    EliminarWinM.iconbitmap("14.ico")
    EliminarWinM.geometry("512x512")
    e1=tk.Label(EliminarWinM, text=" ELIMINAR MERMA :",bg="white",fg="black").place(x=50, y=50)
    
#### VARIABLE PARA ID
    
    entry_id=tk.StringVar()
    productotx=tk.Entry(EliminarWinM,textvariable=entry_id).place(x=50, y=150)

#### ETIQUETA PARA ID

    etiquetanombre=tk.Label(EliminarWinM, text="INGRESE CODIGO DE MERMA", padx=10 ).place(x=30, y=115)
#
    def eliminarM():
        db = sqlite3.connect("articulos.db")
        c = db.cursor()

        
        codigo_merma = entry_id.get()
        c.execute("DELETE  from tbMerma where codigo = ('"+codigo_merma+"')")
        messagebox.showinfo("MODIFICACION","MERMA ELIMINADA" )

        db.commit()
        c.close()
        EliminarWinM.destroy()
        venBorrarM()
        
#### BOTON PARA MENU
    
    menu=tk.Button(EliminarWinM, text="MENU", fg="red",font=("arial", 12),cursor = "hand2",relief = "raised",command = EliminarWinM.destroy)
    menu.pack()
    menu.place(x=50,y=350)
#### BOTON PARA ELIMINAR
    bt_eliminar = tk.Button(EliminarWinM, text =  "ELIMINAR MERMA", fg="blue",font=("arial", 12),cursor = "hand2",relief = "raised",command = eliminarM)
    bt_eliminar.pack()
    bt_eliminar.place(x=280,y=350)
     
 ###################### VENTANA PARA MODIFICAR

def venEditarM():
    #windows.withdraw()
    editarWinM=tk.Toplevel()
    editarWinM.title("MODIFICAR MERMA")
    editarWinM.resizable(0,0)
   
    editarWinM.geometry("640x480")
    lbl_Encabezado=tk.Label(editarWinM, text=" MODIFICAR MERMA :",bg="white",fg="black").place(x=50, y=50)
    
#texbox para id
    
    ProctID=tk.StringVar()
    cuadroID=tk.Entry(editarWinM,textvariable=ProctID).place(x=50, y=120)

#textbox para codigo

    lblcode=tk.Label(editarWinM, text="INGRESE CODIGO DE MERMA", padx=10 ).place(x=30, y=100)

#txtxbox para nombre
    Proctname=tk.StringVar()
    cuadroVx=tk.Entry(editarWinM,textvariable=Proctname).place(x=50, y=170)
#textbox para la cantidad
    
    Proctncand=tk.StringVar()
    cuadroVx=tk.Entry(editarWinM,textvariable=Proctncand).place(x=50, y=230)

###############################################################

    #labels para los valores a modificar

    lblname=tk.Label(editarWinM, text="INGRESE EL NUEVO NOMBRE PARA LA MERMA", padx=10 ).place(x=30, y=150)
    lblcant=tk.Label(editarWinM, text="INGRESE LA NUEVA CANTIDAD PARA LA MERMA", padx=10 ).place(x=30, y=200)
    
  ################modificar el producto consulta
    def modificarM():
        db = sqlite3.connect("articulos.db")
        c = db.cursor()

        codigo_merma = ProctID.get()
        nuevo_no = Proctname.get()
        nuevo_ca = Proctncand.get()
    
        c.execute("update tbMerma set (nombre,cantidad) =('"+nuevo_no+"','"+nuevo_ca+"') where codigo = ('"+codigo_merma+"')")
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACION","MERMA MODIFICADA" )
        editarWinM.destroy()
        venEditarM()

#### BOTON PARA MENU
    
    menu=tk.Button(editarWinM, text="MENU", fg="red",command = editarWinM.destroy)
    menu.pack()
    menu.place(x=50,y=350)
#### BOTON PARA MODIFICAR
    bt_modificar = tk.Button(editarWinM, text =  "MODIFICAR MERMA", fg="green",command = modificarM)
    bt_modificar.pack()
    bt_modificar.place(x=280,y=350)    

##############################################################################################################################


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
	bt_add=tk.Button(inv,text="Agregar Producto", command = venRegistrar)
	bt_add.pack()
	bt_add.place(x=5,y=50)
	#boton para dirigirse a la interfaz de mostrar producto
	bt_view=tk.Button(inv,text="Mostrar Productos", command = venMostrar)
	bt_view.pack()
	bt_view.place(x=5,y=150)
	#boton para dirigirse a la interfaz de eliminar producto
	bt_delet=tk.Button(inv,text="Eliminar Producto",  command = venBorrar)
	bt_delet.pack()
	bt_delet.place(x=5,y=250)
	#boton para dirigirse a la interfaz de modificar producto
	bt_edit=tk.Button(inv,text="Modificar Producto",  command = venEditar)
	bt_edit.pack()
	bt_edit.place(x=5,y=350)
	#boton para dirigirse a la interfaz de agregar mermas
	bt_edit=tk.Button(inv,text="Agregar Mermas",  command = venRegistrarM)
	bt_edit.pack()
	bt_edit.place(x=250,y=50)
	#boton para dirigirse a la interfaz de mostrar mermas
	bt_edit=tk.Button(inv,text="Mostrar Mermas",  command = venMostrarM)
	bt_edit.pack()
	bt_edit.place(x=250,y=150)
	#boton para dirigirse a la interfaz de eliminar mermas
	bt_edit=tk.Button(inv,text="Eliminar Mermas",  command = venBorrarM)
	bt_edit.pack()
	bt_edit.place(x=250,y=250)
	#boton para dirigirse a la interfaz de editar mermas
	bt_edit=tk.Button(inv,text="Editar Mermas",  command = venEditarM)
	bt_edit.pack()
	bt_edit.place(x=250,y=350)
		
raiz.mainloop()
