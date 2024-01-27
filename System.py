from tkinter import *
from PIL import ImageTk, Image #pip install pillow
import pymysql
from tkinter import messagebox
from tkinter import ttk
import pymysql
import calendar
import datetime
from tkcalendar import Calendar # pip install tkcalendar


sesion_iniciada = []


		

def ventana_principal_fun(): #Creamos la primer ventana (Inicio)
	global ventana_principal
	ventana_principal=Tk()
	#-------está porción de código va a centrar mi ventana---------
	w = 500
	h = 350
	ws = ventana_principal.winfo_screenwidth()
	hs = ventana_principal.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_principal.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana_principal.title("Bienvenidos")
	ventana_principal.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es

	#---------------------------------#C8C8E7---------------------
	#abrimos la imagen
	imagenA = Image.open("Imágenes/net.gif")
	#cambiamos el tamaño
	resized = imagenA.resize((450, 225))
	imagenA = ImageTk.PhotoImage(resized)
	label=Label(ventana_principal,image=imagenA).place(x=20,y=10)
	#-----------------------------------------------------

	#https://wiki.tcl-lang.org/page/Colors+with+Names fuentes de colores
	Button(ventana_principal,text="Iniciar Sesión", height="1", width="30",bg="navy", fg="white", font=("Calibri", 15), command=lambda: cross("login", ventana_principal)).place(x=100,y=270)

	mainloop()
def ventana_login_fun(): #Creamos la tercer ventana 3 (login)
	global ventana_login
	global sesion_iniciada
	ventana_login=Tk()
	#-------está porción de código centrara mi ventana---------
	w = 300
	h = 300
	ws = ventana_login.winfo_screenwidth()
	hs = ventana_login.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_login.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana_login.title("Ingresar al Sistema")
	ventana_login.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es

	#------------------------------------------------------
	#abrimos la imagen
	imagen = Image.open("Imágenes/login.png")
	#cambiamos el tamaño
	resized = imagen.resize((105, 120))
	imagen = ImageTk.PhotoImage(resized)
	label=Label(ventana_login,image=imagen).place(x=100,y=10)
	#-----------------------------------------------------
	def validar_admin(): #Validar usuario login
		if (usuario.get()== ""):
			messagebox.showinfo("Faltan datos","ingrese Usuario")
			entry_usuario.focus()
		elif (contrasena.get()== ""):
			messagebox.showinfo("Faltan datos","ingrese Contraseña")
			entry_contrasena.focus()
			return
		else:
			conexion= pymysql.connect(host= "localhost",user="root", passwd="", db= "sistema_gestion_libreria")
			fcursor= conexion.cursor()

			fcursor.execute("SELECT * FROM administradores WHERE Usuario= '"+ usuario.get()+"' and Contrasena= '"+ contrasena.get()+"' ")

			if fcursor.fetchall():
				global sesion_iniciada
				sesion_iniciada = [usuario.get(), contrasena.get()]
				print(sesion_iniciada)
				#Operations([entry_contrasena, entry_usuario], [usuario, contrasena])
				cross("menuLargo", ventana_login)
			else:
				messagebox.showerror("Error","Usuario / Contraseña incorecta")
			conexion.close()
	
	Label(ventana_login, text="Usuario").place(x=50,y=160)
	Label(ventana_login, text="Contraseña").place(x=50,y=200)

	usuario = StringVar()
	entry_usuario = Entry(ventana_login,textvariable= usuario)
	entry_usuario.pack()
	entry_usuario.place(x=140,y=160)

	contrasena = StringVar()
	entry_contrasena = Entry(ventana_login,textvariable= contrasena,  show="*")
	entry_contrasena.pack()
	entry_contrasena.place(x=140,y=200)
	

	Button(ventana_login,text="Entrar", width="15", command=validar_admin,bg="green", fg="white").place(x=25,y=250)
	Button(ventana_login,text="Salir", width="15", command=(lambda: ventana_login.destroy()),bg="navy", fg="white").place(x=160,y=250)
	
	mainloop()
def ventana_menu_principal_fun():
	global ventana_menu_principal
	ventana_menu_principal=Tk()

	#-------está porción de código va a centrar mi ventana---------
	w = 650
	h = 300
	ws = ventana_menu_principal.winfo_screenwidth()
	hs = ventana_menu_principal.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_menu_principal.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------

	ventana_menu_principal.title("Gestión Librería")
	ventana_menu_principal.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es

	#------------------------------------------------------

	#-----------------------------------------------------
	#https://wiki.tcl-lang.org/page/Colors+with+Names fuentes de colores

	Button(ventana_menu_principal,text="Clientes", width="15", command=lambda: cross("clientes", ventana_menu_principal),bg="navy", fg="white").place(x=20,y=20)
	Button(ventana_menu_principal,text="Libros", width="15", command=lambda: cross("libros", ventana_menu_principal),bg="navy", fg="white").place(x=145,y=20)
	Button(ventana_menu_principal,text="Alquileres", width="15", command=(lambda: cross("alquileres", ventana_menu_principal)),bg="navy", fg="white").place(x=270,y=20)
	Button(ventana_menu_principal,text="Administradores", width="15", command=(lambda: cross("verificador", ventana_menu_principal)),bg="navy", fg="white").place(x=395,y=20)
	Button(ventana_menu_principal,text="Salir", width="15", command=(ventana_menu_principal.destroy),bg="navy", fg="white").place(x=520,y=20)


	mainloop()
def ventana_clientes_fun():
	global ventana_clientes
	ventana_clientes=Tk()

	#-------está porción de código va a centrar mi ventana---------
	w = 755
	h = 600
	ws = ventana_clientes.winfo_screenwidth()
	hs = ventana_clientes.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_clientes.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------

	ventana_clientes.title("Clientes")
	ventana_clientes.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	#------------------------------------------------------

	#-------------------------------------------------------

	def estado_inicial_botones_cajas(): #estado de botones cuando se presiona nuevo
		global guardar
		guardar = "nuevo"
		btn_modificar.configure(state='normal')
		btn_eliminar.configure(state='normal')
		btn_guardar.configure(state='disabled')
		btn_nuevo.configure(state='normal')
		btn_cancelar.configure(state='normal')

		entry_apellido.configure(state='disabled')
		entry_nombre.configure(state='disabled')
		entry_dni.configure(state='disabled')
		comboSocio.configure(state='disabled')

		Id.set('')
		Apellido.set('')
		Nombre.set('')
		DNI.set('')
		Socio.set('')
	def btn_nuevo_estado_botones_cajas(): #estado de botones cuando se presiona nuevo
		global guardar
		guardar = "nuevo"

		btn_nuevo.configure(state='disabled')
		btn_modificar.configure(state='disabled')
		btn_eliminar.configure(state='disabled')
		btn_guardar.configure(state='normal')
		btn_cancelar.configure(state='normal')

		entry_apellido.configure(state='normal')
		entry_nombre.configure(state='normal')
		entry_dni.configure(state='normal')
		comboSocio.configure(state='normal')
		comboSocio.set("Seleccione")
	def guardar_cliente(): #Función para dar de alta a un nuevo estidiante
		global guardar
		if guardar == "nuevo":
			if (Apellido.get()== ""):
				messagebox.showinfo("Faltan datos","ingrese Apellido")
				entry_apellido.focus()
				return
			elif (Nombre.get()== ""):
				messagebox.showinfo("Faltan datos","ingrese Nombre")
				entry_nombre.focus()
				return
			elif (DNI.get()== ""):
				messagebox.showinfo("Faltan datos","ingrese DNI")
				entry_dni.focus()
				return
			elif (Socio.get()== "Seleccione"):
				messagebox.showinfo("Faltan datos","Seleccione un Socio")
				comboSocio.focus()

				return
			basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
			fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla
			print(fcursor)
			fcursor.execute("SELECT DNI FROM Clientes  WHERE DNI='"+ DNI.get()+"'")

			if fcursor.fetchall(): # si en la consulta se encuentra ese dni ya registrado no se podar guardar
				messagebox.showwarning("Aviso","Usuario ya Registrado 'Verificar n° de DNI'")
				entry_dni.focus()
			else:
				sql= "INSERT INTO Clientes (Apellido, Nombre, DNI, Socio) VALUES ('{0}','{1}', '{2}', '{3}')".format(Apellido.get(), Nombre.get(), DNI.get(), Socio.get())
				fcursor.execute(sql)
				basedatos.commit()
				messagebox.showinfo("Registro","Se registro el cliente con exito")
				basedatos.close()
				estado_inicial_botones_cajas()
				guardar = "sin valor"

		if guardar == "modificar":
			selected = grid.focus()
			id_seleccionado= grid.item(selected, 'text')
			print("JJJJ", id_seleccionado)
			basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
			fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla

			if dni_1 != DNI.get():
				fcursor.execute("SELECT * FROM Clientes  WHERE DNI='"+ DNI.get()+"'")
				if fcursor.fetchall(): # si en la consulta se encuentra ese dni ya registrado no se podar guardar
					messagebox.showwarning("Aviso","Usuario ya Registrado 'Verificar n° de DNI'")
					entry_dni.focus()
					return
				else:
					print(id_seleccionado , " Id seleccionado")
					sql= "UPDATE Clientes  SET Apellido='{0}', Nombre='{1}', DNI='{2}', Socio='{3}'  WHERE Id_clientes = '{4}'".format(Apellido.get(), Nombre.get(), DNI.get(), Socio.get(),id_seleccionado)
					fcursor.execute(sql)
					basedatos.commit()
					cargar_tabla_clientes()
					messagebox.showinfo("Modificar","Registro Modificado!!")
					id_cliente = -1
					estado_inicial_botones_cajas()
			else:
				sql= "UPDATE Clientes  SET Apellido='{0}', Nombre='{1}', DNI='{2}', Socio='{3}'  WHERE Id_clientes = '{4}'".format(Apellido.get(), Nombre.get(), DNI.get(), Socio.get(),id_seleccionado)
				fcursor.execute(sql)
				basedatos.commit()
				cargar_tabla_clientes()
				messagebox.showinfo("Modificar","Registro Modificado!!")
				id_cliente = -1
				estado_inicial_botones_cajas()
		guardar = "sin valor"
		cargar_tabla_clientes()
	def cargar_tabla_clientes(): #la llamamos al final de la creación del treeview y al final del botón guardar
		basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
		fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla

		fcursor.execute("SELECT * FROM Clientes")

		for item in grid.get_children():
			grid.delete(item)

		for row in fcursor:
			grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3],row[4]))
		basedatos.close() #llamar está función al finalizar el guardado
	def eliminar_cliente():#antes de crear la funcion eliminar debemos habilitar el botón eliminar y llamarlo en el botón
		selected = grid.focus()
		id_seleccionado= grid.item(selected, 'text')
		print(id_seleccionado)

		if id_seleccionado == '':
			messagebox.showwarning("Eliminar","Debes seleccionar un cliente")

		else:
			#print(id_seleccionado)
			btn_modificar.configure(state='disabled')
			valores = grid.item(selected, 'values')
			dato= valores[0] + " " + valores[1] + ", DNI: " + valores[2]
			respuesta = messagebox.askquestion("Eliminar","¿Deseas eliminar el cliente seleccionado?\n" + dato)

			if respuesta == messagebox.YES:
				basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
				fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla


				sql= "DELETE FROM Clientes WHERE Id_Clientes = {0}".format(id_seleccionado)
				fcursor.execute(sql)
				basedatos.commit()
				cargar_tabla_clientes()
				messagebox.showinfo("Eliminar","Registro eliminado!!")
			else:
				messagebox.showinfo("Cancelado","Operación Cancelada")
			estado_inicial_botones_cajas()
	def habilitar_cajas():
		entry_apellido.configure(state='normal')
		entry_nombre.configure(state='normal')
		entry_dni.configure(state='normal')
		comboSocio.config(state='normal')
	def modificar_cliente():#Antes debemos modificar el tipo de selección del treeview
		selected = grid.focus()
		id_seleccionado = grid.item(selected, 'text')

		#print(id_seleccionado)#solo para verificar en consola

		if id_seleccionado == '':
			messagebox.showwarning("Modificar","Debes seleccionar un cliente")
			return

		global dni_1
		global guardar
		guardar = "modificar"
		btn_eliminar.configure(state='disabled')
		btn_guardar.configure(state='normal')
		habilitar_cajas()
		valores = grid.item(selected, 'values')
		print(valores)

		Apellido_2 = valores[0]
		Nombre_2 = valores[1]
		DNI_2 = valores[2]
		Socio_2 = valores[3]

		Id.set(id_seleccionado)
		Apellido.set(Apellido_2)
		Nombre.set(Nombre_2)
		DNI.set(DNI_2)
		Socio.set(Socio_2)

		#tomamos el dni y lo guardamos en una nueva variable
		dni_1 = DNI.get()
	def filtros_consulta(vals, table, cantCombos):
		global buscar
		whatIs = [0, 0 ,0]
		if buscar == False:
			apellido_filtrar.set(""), dni_flitrar.set(""), socio_filtrar.set("") #comboSocioFiltrar
			entry_apellido_filtar.configure(state="normal")
			entry_dni_filtar.configure(state="normal")
			comboSocioFiltrar.configure(state="normal")
			comboSocioFiltrar.set("Seleccione")
			btn_limpiar.configure(state="normal")

			buscar= True
			return
		for i,e in enumerate(vals):
			cach = str((vals.get(e)).get())
			print("Cach:", cach)
			print("indice:", i)
			if (len(vals)-1) == i and cach == "Seleccione": #Si esta en el ultimo indice y esta por defecto:
				pass
				print("passed1")
			elif cach != "":
				whatIs[0] = cach
				whatIs[1]+=1
				whatIs[2] = e
				print(cach)
			if whatIs[1] > 1:
				messagebox.showinfo("Aviso","solo se puede filtrar por un valor y debes ingresar al menos un dato")
				
				return
		print(vals.get(whatIs[0]))
		print("arriba")
		basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria")
		fcursor=basedatos.cursor()
		fcursor.execute("SELECT * FROM "+str(table)+"  WHERE "+str(whatIs[2])+"='"+whatIs[0]+"'")
		for item in grid.get_children():
			grid.delete(item)

		for row in fcursor:
			grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3],row[4]))
		basedatos.close()
		
	def limpiar_busqueda():
		global buscar
		apellido_filtrar.set("")
		dni_flitrar.set("")
		socio_filtrar.set("")

		entry_apellido_filtar.configure(state="disabled")
		entry_dni_filtar.configure(state="disabled")
		comboSocioFiltrar.configure(state="disabled")
		btn_limpiar.configure(state="disabled")

		cargar_tabla_clientes()

		buscar= False
	#-------------------------------------------------------
	btn_nuevo = Button(ventana_clientes,text="Nuevo", width="15", command=btn_nuevo_estado_botones_cajas,bg="navy", fg="white")
	btn_nuevo.pack()
	btn_nuevo.place(x=20,y=20)

	btn_modificar = Button(ventana_clientes,text="Modificar", width="15", command=modificar_cliente,bg="navy", fg="white")
	btn_modificar.pack()
	btn_modificar.place(x=140,y=20)

	btn_eliminar = Button(ventana_clientes,text="Eliminar", width="15", command=eliminar_cliente,bg="red", fg="white")
	btn_eliminar.pack()
	btn_eliminar.place(x=260,y=20)

	btn_guardar = Button(ventana_clientes,text="Guardar", width="15", command=guardar_cliente,bg="green", fg="white")
	btn_guardar.pack()
	btn_guardar.place(x=380,y=20)

	btn_cancelar = Button(ventana_clientes,text="Cancelar",width="15", command=estado_inicial_botones_cajas,bg="red", fg="white")
	btn_cancelar.pack()
	btn_cancelar.place(x=500,y=20)

	btn_salir = Button(ventana_clientes,text="Salir",width="15", command=(lambda: cross("menuLargo", ventana_clientes)),bg="red", fg="white")
	btn_salir.pack()
	btn_salir.place(x=620,y=20)

	#Crear marco de etiqueta
	LabelFrame( ventana_clientes, width= 715, height=70).place(x=20,y=50)

	Label(ventana_clientes, text="ID").place(x=30,y=60)
	Label(ventana_clientes, text="Apellido").place(x=180,y=60)
	Label(ventana_clientes, text="Nombre").place(x=320,y=60)
	Label(ventana_clientes, text="DNI").place(x=470,y=60)
	Label(ventana_clientes, text="Socio").place(x=590,y=60)

	global Id, Apellido, Nombre, Socio, DNI
	Id = StringVar()
	Apellido = StringVar()
	Nombre = StringVar()
	DNI = StringVar()
	Socio = StringVar()

	valoresSocio= ['Si','No']

	entry_id=Entry(ventana_clientes,textvariable= Id, state='disabled')
	entry_id.pack()
	entry_id.place(x=25,y=80)

	entry_apellido = Entry(ventana_clientes,textvariable= Apellido)
	entry_apellido.pack()
	entry_apellido.place(x=160,y=80)

	entry_nombre=Entry(ventana_clientes,textvariable= Nombre)
	entry_nombre.pack()
	entry_nombre.place(x=295,y=80)

	entry_dni=Entry(ventana_clientes,textvariable= DNI)
	entry_dni.pack()
	entry_dni.place(x=430,y=80)

	comboSocio = ttk.Combobox(ventana_clientes,textvariable= Socio, values=valoresSocio)
	comboSocio.pack()
	comboSocio.place(x=570,y=80)

	#-------------Treeview-------------------------------------------------
	grid = ttk.Treeview(ventana_clientes, columns=("col1", "col2", "col3","col4")) #from tkinter import ttk

	grid.column("#0", width=50)
	grid.column("col1", width=140, anchor=CENTER)
	grid.column("col2", width=140, anchor=CENTER)
	grid.column("col3", width=140, anchor=CENTER)
	grid.column("col4", width=140, anchor=CENTER)

	grid.heading("#0", text="Id")
	grid.heading("col1", text="Apellido", anchor=CENTER)
	grid.heading("col2", text="Nombre", anchor=CENTER)
	grid.heading("col3", text="DNI", anchor=CENTER)
	grid.heading("col4", text="Socio", anchor=CENTER)

	grid.pack()
	grid.place(x=20,y=130, width=715, height=350)
	grid['selectmode']='browse'#Modifica el tipo de selección
	#-------------Treeview-------------------------------------------------

	#---------Dideña para filtrar------------------------------------------
	#Crear marco de etiqueta
	LabelFrame( ventana_clientes, text="Consultas", width= 715, height=100).place(x=20,y=485)

	global apellido_filtrar, dni_flitrar, socio_filtrar
	apellido_filtrar = StringVar()
	dni_flitrar = StringVar()
	socio_filtrar = StringVar()
	valoressocio_filtrar= ['No','Si']


	Label(ventana_clientes, text="Apellido").place(x=30,y=510)
	Label(ventana_clientes, text="DNI").place(x=180,y=510)
	Label(ventana_clientes, text="Socio").place(x=330,y=510)

	entry_apellido_filtar = Entry(ventana_clientes,textvariable= apellido_filtrar)
	entry_apellido_filtar.pack()
	entry_apellido_filtar.place(x=30,y=530)


	entry_dni_filtar = Entry(ventana_clientes,textvariable= dni_flitrar)
	entry_dni_filtar.pack()
	entry_dni_filtar.place(x=180,y=530)

	comboSocioFiltrar = ttk.Combobox(ventana_clientes,textvariable=socio_filtrar,values=valoressocio_filtrar)
	comboSocioFiltrar.set("Seleccione")
	comboSocioFiltrar.pack()
	comboSocioFiltrar.place(x=330,y=530)

	btn_buscar = Button(ventana_clientes,text="Buscar",width="10", command=lambda: filtros_consulta({"Apellido": apellido_filtrar, "DNI": dni_flitrar, "Socio": socio_filtrar}, "Clientes", 1),bg="navy", fg="white")
	btn_buscar.pack()
	btn_buscar.place(x=500,y=520)

	btn_limpiar = Button(ventana_clientes,text="Limpiar",width="10", command=limpiar_busqueda,bg="navy", fg="white")
	btn_limpiar.pack()
	btn_limpiar.place(x=600,y=520)
	#------------------------------------------------------------------------

	cargar_tabla_clientes()
	estado_inicial_botones_cajas()
	limpiar_busqueda()
	mainloop()
def libros_ventana_fun():
		
		global ventana_libros
		ventana_libros = Tk()
		ventana_libros.resizable(0,0)
		#---------------------------------------
		w = 990
		h  = 700
		ws = ventana_libros.winfo_screenwidth()
		hs = ventana_libros.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana_libros.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#----------------------------------------
		def estado_inicial_botones_cajas():
			global guardar
			guardar = "nuevo"
			boton_modificar.configure(state='normal')
			boton_eliminar.configure(state='normal')
			boton_guardar.configure(state='disabled')
			boton_nuevo.configure(state='normal')
			boton_cancelar.configure(state='normal')

			entry_autor.configure(state='disabled')
			entry_codigo.configure(state='disabled')
			entry_nombre.configure(state='disabled')
			entry_precio.configure(state='disabled')
			comboestado.configure(state='disabled')
			combogenero.configure(state='disabled')

			autor_string.set('')
			codigo_string.set('')
			nombre_string.set('')
			precio_string.set('')
			id_string.set('')
			comboestado.set('')
			combogenero.set('')
		def eliminar_cliente():
			selected = grid.focus()
			id_seleccionado= grid.item(selected, 'text')
			print(id_seleccionado)

			if id_seleccionado == '':
				messagebox.showwarning("Eliminar","Debes seleccionar un cliente")

			else:
				#print(id_seleccionado)
				boton_modificar.configure(state='disabled')
				valores = grid.item(selected, 'values')
				dato= valores[1] + ", De: " + valores[2] + ", CODIGO: " + valores[1]
				respuesta = messagebox.askquestion("Eliminar","¿Deseas eliminar el libro seleccionado?\n" + dato)

				if respuesta == messagebox.YES:
					basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
					fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla


					sql= "DELETE FROM Libros WHERE Id = {0}".format(id_seleccionado)
					fcursor.execute(sql)
					basedatos.commit()
					cargar_tabla()
					messagebox.showinfo("Eliminar","Libro eliminado!")
				else:
					messagebox.showinfo("Cancelado","Operación Cancelada")
				estado_inicial_botones_cajas()
		def habilitar_cajas():
			entry_autor.configure(state='normal')
			entry_codigo.configure(state='normal')
			entry_nombre.configure(state='normal')
			entry_precio.configure(state='normal')
			comboestado.config(state='normal')
			combogenero.config(state='normal')
		def cargar_tabla():
			basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
			fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla

			fcursor.execute("SELECT * FROM Libros")

			for item in grid.get_children():
				grid.delete(item)

			for row in fcursor:
				grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3],row[4], row[5], row[6]))
			basedatos.close() #llamar está función al finalizar el guardado
		def nuevo_btn():
				global guardar
				guardar = "nuevo"

				boton_nuevo.configure(state='disabled')
				boton_modificar.configure(state='disabled')
				boton_eliminar.configure(state='disabled')
				boton_guardar.configure(state='normal')
				boton_cancelar.configure(state='normal')

				entry_codigo.configure(state='normal')
				entry_autor.configure(state='normal')
				entry_nombre.configure(state='normal')
				entry_precio.configure(state='normal')
				combogenero.configure(state='normal')
				comboestado.configure(state='normal')
		def modificar_btn():
			selected = grid.focus()
			id_seleccionado = grid.item(selected, 'text')

			#print(id_seleccionado)#solo para verificar en consola

			if id_seleccionado == '':
				messagebox.showwarning("Modificar","Debes seleccionar un cliente")
				return

			global codigo_1
			global guardar
			guardar = "modificar"
			boton_eliminar.configure(state='disabled')
			boton_guardar.configure(state='normal')
			habilitar_cajas()
			valores = grid.item(selected, 'values')
			print(valores)

			Codigo_2 = valores[0]
			Autor_2 = valores[1]
			Nombre_2 = valores[2]
			Precio_2 = valores[3]
			Genero_2 = valores[4]
			Estado_2 = valores[5]

			id_string.set(id_seleccionado)
			codigo_string.set(Codigo_2)
			autor_string.set(Autor_2)
			precio_string.set(Precio_2)
			nombre_string.set(Nombre_2)
			combogenero.set(Genero_2)
			comboestado.set(Estado_2)

			#tomamos el dni y lo guardamos en una nueva variable
			codigo_1 = codigo_string.get()
		def guardar_cliente():
			global guardar
			if guardar == "nuevo":
				if (codigo_string.get()== ""):
					messagebox.showinfo("Faltan datos","ingrese Apellido")
					entry_codigo.focus()
					return
				elif (autor_string.get()== ""):
					messagebox.showinfo("Faltan datos","ingrese Nombre")
					entry_autor.focus()
					return
				elif (nombre_string.get()== ""):
					messagebox.showinfo("Faltan datos","ingrese DNI")
					entry_nombre.focus()
					return
				elif (precio_string.get()== ""):
					messagebox.showinfo("Faltan datos","ingrese DNI")
					entry_precio.focus()
					return
				elif (comboestado.get()== "Seleccione"):
					messagebox.showinfo("Faltan datos","Seleccione un Socio")
					comboestado.focus()
					return
				elif (combogenero.get()== "Seleccione"):
					messagebox.showinfo("Faltan datos","Seleccione un Socio")
					combogenero.focus()
					return
				basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
				fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla
				print(fcursor)
				fcursor.execute("SELECT CODIGO FROM Libros WHERE CODIGO='"+ codigo_string.get()+"'")

				if fcursor.fetchall(): # si en la consulta se encuentra ese dni ya registrado no se podar guardar
					messagebox.showwarning("Aviso","Usuario ya Registrado 'Verificar n° de DNI'")
					entry_codigo.focus()
				else:
					sql= "INSERT INTO Libros (Codigo, Autor, Nombre, Precio, Genero, Estado) VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}')".format(codigo_string.get(), autor_string.get(), nombre_string.get(), precio_string.get(), combogenero.get(), comboestado.get())
					fcursor.execute(sql)
					basedatos.commit()
					messagebox.showinfo("Registro","Se registro el libro con exito")
					basedatos.close()
					guardar = "sin valor"

			if guardar == "modificar":
				selected = grid.focus()
				id_seleccionado= grid.item(selected, 'text')
				print("JJJJ", id_seleccionado)
				basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
				fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla

				if codigo_1 != codigo_string.get():
					fcursor.execute("SELECT * FROM Libros  WHERE CODIGO='"+ codigo_string.get()+"'")
					if fcursor.fetchall(): # si en la consulta se encuentra ese dni ya registrado no se podar guardar
						messagebox.showwarning("Aviso","Libro ya Registrado 'Verificar n° de Codigo'")
						entry_codigo.focus()
						return
					else:
						print(id_seleccionado , " Id seleccionado")
						sql= "UPDATE Libros SET Codigo='{0}', Autor='{1}', Nombre='{2}', Precio='{3}', Genero='{4}', Estado='{5}'  WHERE id = '{6}'".format(codigo_string.get(), autor_string.get(), nombre_string.get(), precio_string.get(), combogenero.get(), comboestado.get(), id_seleccionado)
						fcursor.execute(sql)
						basedatos.commit()
						cargar_tabla()
						messagebox.showinfo("Modificar","Registro Modificado!!")
						id_cliente = -1
						estado_inicial_botones_cajas()
				else:
					sql= "UPDATE Libros  SET Codigo='{0}', Autor='{1}', Nombre='{2}', Precio='{3}', Genero='{4}', Estado='{5}'  WHERE id = '{6}'".format(codigo_string.get(), autor_string.get(), nombre_string.get(), precio_string.get(), combogenero.get(), comboestado.get(), id_seleccionado)
					fcursor.execute(sql)
					basedatos.commit()
					cargar_tabla()
					messagebox.showinfo("Modificar","Registro Modificado!!")
					id_cliente = -1
					estado_inicial_botones_cajas()
			cargar_tabla()
			estado_inicial_botones_cajas()
		def filtros_consulta(vals, table, cantCombos):
			global buscar
			whatIs = [0, 0 ,0]
			if buscar == False:
				codigo_buscar.set(""), titulo_buscar.set(""), autor_buscar.set("") #comboSocioFiltrar
				entry_buscar_codigo.configure(state="normal")
				entry_buscar_titulo.configure(state="normal")
				entry_buscar_autor.configure(state="normal")
				combo_genero_buscar.configure(state="normal")
				combo_estado_buscar.configure(state="normal")
				combo_genero_buscar.set("Seleccione")
				combo_estado_buscar.set("Seleccione")
				button_limpiar.configure(state="normal")

				buscar= True
				return
			for i,e in enumerate(vals):
				print(vals)
				cach = str((vals.get(e)).get())
				print("Cach:", cach)
				print("indice:", i)
				if (len(vals)-1) == i and cach == "Seleccione": #Si esta en el ultimo indice y esta por defecto:
					pass
					print("passed1")
					print("paso igual")
				elif (len(vals)-2) == i and cach == "Seleccione":
					pass	
					print("passed2")
					
				elif cach != "":
					whatIs[0] = cach
					whatIs[1]+=1
					whatIs[2] = e
					print("What updated:", whatIs)
				if whatIs[1] > 1:
					messagebox.showinfo("Aviso","solo se puede filtrar por un valor")
					
					return
			print("vals = ", vals.get(whatIs[0]))
			print("vals2 = ", whatIs)
			print("arriba")
			basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria")
			fcursor=basedatos.cursor()
			print("SELECT * FROM "+str(table)+"  WHERE "+str(whatIs[2])+"='"+whatIs[0]+"'")
			fcursor.execute("SELECT * FROM "+str(table)+"  WHERE "+str(whatIs[2])+"='"+whatIs[0]+"'")
			for item in grid.get_children():
				grid.delete(item)

			for row in fcursor:
				grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
			basedatos.close()
		def limpiar_busqueda():
			global buscar
			codigo_buscar.set(""), titulo_buscar.set(""), autor_buscar.set("") #comboSocioFiltrar

			entry_buscar_autor.configure(state="disabled")
			entry_buscar_codigo.configure(state="disabled")
			entry_buscar_titulo.configure(state="disabled")
			combo_estado_buscar.configure(state="disabled")
			combo_genero_buscar.configure(state="disabled")

			combo_estado_buscar.set("")
			combo_genero_buscar.set("")																	

			button_limpiar.configure(state="disabled")
			button_buscar.configure(state="normal")
			buscar= False
			cargar_tabla()
		guardar = "sin valor"


		ventana_libros.title("Libros")
		ventana_libros.iconbitmap("Imágenes/logoProA.ico")

		boton_nuevo = Button(ventana_libros, text="Nuevo", width=15, height=1,bg="#0A0AF0", state=NORMAL, command=(nuevo_btn), fg="white")
		boton_nuevo.pack()
		boton_nuevo.place(x=160,y=10)

		boton_modificar = Button(ventana_libros, text="Modificar", width=15, height=1,bg="#0A0AF0", state=NORMAL, command=(modificar_btn), fg="white")
		boton_modificar.pack
		boton_modificar.place(x=290,y=10)

		boton_eliminar = Button(ventana_libros, text="Eliminar", width=15, height=1,bg="#FF1F24", command=(eliminar_cliente), fg="white")
		boton_eliminar.pack
		boton_eliminar.place(x=420,y=10)

		boton_guardar = Button(ventana_libros, text="Guardar", width=15, height=1,bg="#5ab507", state=DISABLED, command=(guardar_cliente), fg="white")
		boton_guardar.pack
		boton_guardar.place(x=550,y=10)

		boton_cancelar = Button(ventana_libros, text="Cancelar", width=15, height=1,bg="#FF1F24", command=(estado_inicial_botones_cajas), fg="white")
		boton_cancelar.pack
		boton_cancelar.place(x=680,y=10)

		boton_salir = Button(ventana_libros, text="Salir", width=10, height=1,bg="#FF1F24", command=(lambda: cross("menuLargo", ventana_libros)), fg="white")
		boton_salir.pack
		boton_salir.place(x=810,y=10)

		grid = ttk.Treeview(ventana_libros, columns=("col1","col2", "col3", "col4", "col5", "col6"))

		grid.column("#0", width=50, anchor=CENTER)
		grid.column("col1", width=150, anchor=CENTER)
		grid.column("col2", width=150, anchor=CENTER)
		grid.column("col3", width=150, anchor=CENTER)
		grid.column("col4", width=150, anchor=CENTER)
		grid.column("col5", width=150, anchor=CENTER)
		grid.column("col6", width=150, anchor=CENTER)

		grid.heading("#0", text="Id", anchor=CENTER)
		grid.heading("col1", text="Codigo", anchor=CENTER)
		grid.heading("col2", text="Autor", anchor=CENTER)
		grid.heading("col3", text="Nombre", anchor=CENTER)
		grid.heading("col4", text="Precio", anchor=CENTER)
		grid.heading("col5", text="Genero", anchor=CENTER)
		grid.heading("col6", text="Estado", anchor=CENTER)
		grid.pack()
		grid.place(x=20, y=130, width=950, height=450)

		label_entry = Label(ventana_libros, text="ID")
		label_entry.pack()
		label_entry.place(x=10,y=50)

		id_string = StringVar()
		entry_id = Entry(ventana_libros, state=DISABLED, textvariable=id_string)
		entry_id.pack()
		entry_id.place(x=10, y=75)

		label_entry = Label(ventana_libros, text="Codigo")
		label_entry.pack()
		label_entry.place(x=140,y=50)

		codigo_string = StringVar()
		entry_codigo = Entry(ventana_libros, state=DISABLED, textvariable=codigo_string)
		entry_codigo.pack()
		entry_codigo.place(x=140, y=75)

		label_entry = Label(ventana_libros, text="Autor")
		label_entry.pack()
		label_entry.place(x=270,y=50)

		autor_string = StringVar()
		entry_autor = Entry(ventana_libros, textvariable=autor_string, state=DISABLED)
		entry_autor.pack()
		entry_autor.place(x=270, y=75)

		label_entry = Label(ventana_libros, text="Titulo")
		label_entry.pack()
		label_entry.place(x=400,y=50)

		nombre_string = StringVar()
		entry_nombre = Entry(ventana_libros, textvariable=nombre_string, state=DISABLED)
		entry_nombre.pack()
		entry_nombre.place(x=400, y=75)

		label_entry = Label(ventana_libros, text="Precio")
		label_entry.pack()
		label_entry.place(x=530,y=50)

		precio_string = StringVar()
		entry_precio = Entry(ventana_libros, textvariable=precio_string, state=DISABLED)
		entry_precio.pack()
		entry_precio.place(x=530, y=75)

		label_entry = Label(ventana_libros, text="Genero")
		label_entry.pack()
		label_entry.place(x=660,y=50)

		generos_lista = ["Drama", "Terror", "Comedia", "Romatico", "Fantasia", "Suspenso", "Acccion", "Documental", "Biografia", "Guia"]
		combogenero = ttk.Combobox(ventana_libros, values=generos_lista, state=DISABLED)
		combogenero.set("Seleccione")
		combogenero.pack()
		combogenero.place(x=660,y=75)

		label_entry = Label(ventana_libros, text="Estado")
		label_entry.pack()
		label_entry.place(x=810,y=50)

		estados_lista = ["Disponible", "Reservado", "Baja"]
		comboestado = ttk.Combobox(ventana_libros, values=estados_lista, state=DISABLED)
		comboestado.set("Seleccione")
		comboestado.pack()
		comboestado.place(x=810,y=75)


		framee = ttk.Labelframe(ventana_libros, width=950, height=80, text="Consultas")
		framee.pack()
		framee.place(x=20 ,y=580)
		print("_---------------------------_")
		label_frame1 = Label(ventana_libros, text="Codigo")
		label_frame1.pack()
		label_frame1.place(x=40 ,y=598)

		codigo_buscar = StringVar()
		entry_buscar_codigo = Entry(ventana_libros, textvariable=codigo_buscar, state=DISABLED)
		entry_buscar_codigo.pack()
		entry_buscar_codigo.place(x=40, y=620)

		label_frame2 = Label(ventana_libros, text="Titulo")
		label_frame2.pack()
		label_frame2.place(x=180 ,y=598)

		titulo_buscar = StringVar()
		entry_buscar_titulo = Entry(ventana_libros, textvariable=titulo_buscar, state=DISABLED)
		entry_buscar_titulo.pack()
		entry_buscar_titulo.place(x=180, y=620)

		label_frame2 = Label(ventana_libros, text="Autor")
		label_frame2.pack()
		label_frame2.place(x=320 ,y=598)

		autor_buscar = StringVar()
		entry_buscar_autor = Entry(ventana_libros, textvariable=autor_buscar, state=DISABLED)
		entry_buscar_autor.pack()
		entry_buscar_autor.place(x=320, y=620)

		label_frame3 = Label(ventana_libros, text="Genero")
		label_frame3.pack()
		label_frame3.place(x=460 ,y=598)

		
		genero_buscar = StringVar()
		estado_buscar = StringVar()

		genero_frame_list = ["Drama", "Terror", "Comedia", "Romatico", "Fantasia", "Suspenso", "Acccion", "Documental", "Biografia", "Guia"]
		combo_genero_buscar = ttk.Combobox(ventana_libros, textvariable=genero_buscar, values=genero_frame_list, state=DISABLED)
		combo_genero_buscar.set("Seleccione")
		combo_genero_buscar.pack()
		combo_genero_buscar.place(x=460 ,y=620)

		label_frame3 = Label(ventana_libros, text="Estado")
		label_frame3.pack()
		label_frame3.place(x=620 ,y=598)

		estado_frame_list = ["Disponible", "Reservado", "Baja"]
		combo_estado_buscar = ttk.Combobox(ventana_libros, textvariable=estado_buscar, values=estado_frame_list, state=DISABLED)
		combo_estado_buscar.set("Seleccione")
		combo_estado_buscar.pack()
		combo_estado_buscar.place(x=620 ,y=620)

		button_buscar = Button(ventana_libros, text="Buscar", width=8, height=2, bg="#0A0AF0", fg="white", command=(lambda: filtros_consulta({"Codigo": codigo_buscar, "Autor": autor_buscar, "Nombre": titulo_buscar, "Genero": genero_buscar, "Estado": estado_buscar}, "Libros", 0)))
		button_limpiar = Button(ventana_libros, text="Limpiar", width=8, height=2, bg="#0A0AF0", fg="white", command=(limpiar_busqueda))
		button_buscar.pack()
		button_limpiar.pack()
		button_buscar.place(x=780 ,y=600)
		button_limpiar.place(x=860 , y=600)

		
		limpiar_busqueda()
		print(buscar) 
		mainloop()
def ventana_menu_fun(): # Creamos la cuarta ventana del menú principal
	global ventana_menu
	ventana_menu=Tk()

	#-------está porción de código va a centrar mi ventana---------
	w = 490
	h = 300
	ws = ventana_menu.winfo_screenwidth()
	hs = ventana_menu.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------

	ventana_menu.title("Gestión Librería")
	ventana_menu.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	#------------------------------------------------------

	#Crear marco de etiqueta
	LabelFrame( ventana_menu, text = "Datos del Cliente", width= 230, height=180).place(x=10,y=10)

	label_apellido = Label(ventana_menu, text = "Apellido")
	label_apellido.pack()
	label_apellido.place(x=20,y=30)

	apellido = StringVar()
	entry_apellido = Entry(ventana_menu,textvariable = apellido)
	entry_apellido.pack()
	entry_apellido.place(x=100,y=30)

	label_nombre = Label(ventana_menu, text = "Nombre")
	label_nombre.pack()
	label_nombre.place(x=20,y=60)

	nombre = StringVar()
	entry_nombre = Entry(ventana_menu, textvariable =nombre)
	entry_nombre.pack()
	entry_nombre.place(x=100,y=60)

	label_dni = Label(ventana_menu, text = "DNI")
	label_dni.pack()
	label_dni.place(x=20,y=90)

	dni = StringVar()
	entry_dni = Entry(ventana_menu, textvariable = dni)
	entry_dni.pack()
	entry_dni.place(x=100,y=90)

	label_socio = Label(ventana_menu, text = "Socio")
	label_socio.pack()
	label_socio.place(x=20,y=120)

	VarSeleccion=IntVar()
	VarSeleccion.set(0)
	Radiobutton(ventana_menu, text="Si",value=1,variable=VarSeleccion).place(x=20,y=150)
	Radiobutton(ventana_menu,text="No",value=2,variable=VarSeleccion).place(x=70,y=150)

	#Crear marco de etiqueta
	LabelFrame( ventana_menu, text = "Datos del servicio", width= 230, height=180).place(x=250,y=10)

	label_genero = Label(ventana_menu, text = "Seleccione Género")
	label_genero.pack()
	label_genero.place(x=260,y=30)

	valores_genero= ['Drama','Comedio','Ficción']
	combo_genero = ttk.Combobox(ventana_menu, values=valores_genero)
	combo_genero.set("Género")
	combo_genero.pack()
	combo_genero.place(x=260,y=60)

	lbl_pecio = Label(ventana_menu, text = "Precio $")
	lbl_pecio.pack()
	lbl_pecio.place(x=260,y=90)

	precio = StringVar()
	entry_precio = Entry(ventana_menu, textvariable = precio)
	entry_precio.pack()
	entry_precio.place(x=340,y=90)

	label_dias = Label(ventana_menu, text = "Días")
	label_dias.pack()
	label_dias.place(x=260,y=120)

	dias = StringVar()
	entry_dias = Entry(ventana_menu, textvariable = dias)
	entry_dias.pack()
	entry_dias.place(x=340,y=120)

	#Crear marco de etiqueta
	LabelFrame( ventana_menu, width= 470, height=50).place(x=10,y=200)

	label_pago = Label(ventana_menu, text = "Pago")
	label_pago.pack()
	label_pago.place(x=20,y=210)

	pago = StringVar()
	entry_pago = Entry(ventana_menu, state= DISABLED, textvariable = pago)
	entry_pago.pack()
	entry_pago.place(x=70,y=210)

	btn_calcular = Button(ventana_menu,width="10",bg="blue" ,fg="white",text="Calcular", command=())
	btn_calcular.pack()
	btn_calcular.place(x=200,y=210)

	btn_guardar = Button(ventana_menu,width="10",bg="blue" ,fg="white",text="Guardar", command=())
	btn_guardar.pack()
	btn_guardar.place(x=290,y=210)
	#--------------------------------------------------------------------

	btn_limpiar = Button(ventana_menu,width="10", bg="green",fg="white",text="Limpiar", command=())
	btn_limpiar.pack()
	btn_limpiar.place(x=30,y=260)

	btn_salir = Button(ventana_menu,width="10", bg="red",fg="white", text="Salir", command=lambda: cross("menuCorto", ventana_menu))
	btn_salir.pack()
	btn_salir.place(x=150,y=260)

	mainloop()
def administradores_ventana():
	global ventana_admins
	ventana_admins = Tk()
	ventana_admins.resizable(0,0)
	#---------------------------------------
	w = 700
	h  = 670
	ws = ventana_admins.winfo_screenwidth()
	hs = ventana_admins.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_admins.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------
	def eliminar_cliente():
		selected = grid.focus()
		id_seleccionado= grid.item(selected, 'text')
		
		if id_seleccionado == '':
			messagebox.showerror("Error","Debes seleccionar un administrador")

		else:
			boton_modificar.configure(state='disabled')
			valores = grid.item(selected, 'values')
			dato= "Usuario: " + valores[0] + ", Mail: " + valores[1]
			respuesta = messagebox.askquestion("Eliminar","¿Deseas eliminar administrador seleccionado?\n" + dato)

			if respuesta == messagebox.YES:
				basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") 
				fcursor=basedatos.cursor() 


				sql= "DELETE FROM Administradores WHERE Id_administrador = {0}".format(id_seleccionado)
				fcursor.execute(sql)
				basedatos.commit()
				cargar_tabla()
				messagebox.showinfo("Eliminar","Cuenta eliminada!")
			estado_inicial_botones_cajas()
	def habilitar_cajas():
		entry_usuario.configure(state='normal')
		entry_mail.configure(state='normal')
		entry_contra.configure(state='normal')
		entry_contra_2.configure(state='disabled')
	def modificar_btn():
		selected = grid.focus()
		id_seleccionado = grid.item(selected, 'text')
		
		if id_seleccionado == '':
			messagebox.showwarning("Modificar","Debes seleccionar un cliente")
			return

		global codigo_admin
		global guardar
		guardar = "modificar"
		boton_eliminar.configure(state='disabled')
		boton_guardar.configure(state='normal')
		habilitar_cajas()
		valores = grid.item(selected, 'values')

		Usuario2 = valores[0]
		Mail2 = valores[1]
		Contra2 = valores[2]

		id_string.set(id_seleccionado)
		usuario_string.set(Usuario2)
		mail_string.set(Mail2)
		contra_string.set(Contra2)

		#tomamos el dni y lo guardamos en una nueva variable
		codigo_admin = mail_string.get()
	def cargar_tabla():
		basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
		fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla

		fcursor.execute("SELECT * FROM Administradores")

		for item in grid.get_children():
			grid.delete(item)

		for row in fcursor:
			grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3]))
		basedatos.close() #llamar está función al finalizar el guardado
	def estado_inicial_botones_cajas():
		global guardar
		guardar = "nuevo"
		boton_modificar.configure(state='normal')
		boton_eliminar.configure(state='normal')
		boton_guardar.configure(state='disabled')
		boton_nuevo.configure(state='normal')
		boton_cancelar.configure(state='normal')

		entry_usuario.configure(state='disabled')
		entry_mail.configure(state='disabled')
		entry_contra.configure(state='disabled')
		entry_contra_2.configure(state='disabled')

		usuario_string.set('')
		mail_string.set('')
		contra_string_2.set('')
		contra_string.set('')
		id_string.set('')
	def guardar_admin():
		global guardar
		if guardar == "nuevo":
			if (usuario_string.get()== ""):
				messagebox.showinfo("Faltan datos","ingrese Usuario")
				entry_usuario.focus()
				return
			elif (mail_string.get()== ""):
				messagebox.showinfo("Faltan datos","ingrese Mail")
				entry_mail.focus()
				return
			elif (contra_string.get()== ""):
				messagebox.showinfo("Faltan datos","ingrese contraseña")
				entry_contra.focus()
				return
			elif (contra_string_2.get()== ""):
				messagebox.showinfo("Faltan datos","repíta la contraseña")
				entry_contra_2.focus()
				return
			elif (contra_string.get() != contra_string_2.get()):
				messagebox.showinfo("Contraseña incorrecta","Verifíque la contraseña")
				entry_contra_2.focus()
				return
			len(contra_string.get())
			basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
			fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla
			print(fcursor)
			fcursor.execute("SELECT NOMBRE FROM Libros WHERE NOMBRE='"+ usuario_string.get()+"'")

			if fcursor.fetchall(): # si en la consulta se encuentra ese dni ya registrado no se podar guardar
				messagebox.showerror("Error","Usuario ya Registrado 'Verificar el correo electronico'")
				entry_mail.focus()
			else:
				sql= "INSERT INTO Administradores (Usuario, Mail, Contrasena) VALUES ('{0}','{1}', '{2}')".format(usuario_string.get(), mail_string.get(), contra_string.get())
				fcursor.execute(sql)
				basedatos.commit()
				messagebox.showinfo("Registro","Se registro el administrador con exito")
				basedatos.close()
				guardar = "sin valor"
		if guardar == "modificar":
			selected = grid.focus()
			id_seleccionado= grid.item(selected, 'text')
			print("JJJJ", id_seleccionado)
			basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistema_gestion_libreria") #creamos la base de datos indicandole la ruta (ubicación)
			fcursor=basedatos.cursor() #objeto de acceso a datos que se puede utilizar para recorrer filas de una tabla

			if codigo_admin != mail_string.get():
				fcursor.execute("SELECT * FROM Administradores  WHERE MAIL='"+ mail_string.get()+"'")
				if fcursor.fetchall(): # si en la consulta se encuentra ese dni ya registrado no se podar guardar
					messagebox.showwarning("Aviso","Administrador ya Registrado 'Verificar el correo electronico'")
					entry_mail.focus()
					return
				else:
					print(id_seleccionado , " Id seleccionado")
					sql= "UPDATE Administradores SET Usuario='{0}', Mail='{1}', Contrasena='{2}'  WHERE id_administrador = '{3}'".format(usuario_string.get(), mail_string.get(), contra_string.get(), id_seleccionado)
					fcursor.execute(sql)
					basedatos.commit()
					messagebox.showinfo("Modificar","Administrador Modificado!!")
					id_cliente = -1
			else:
				sql= "UPDATE Administradores SET Usuario='{0}', Mail='{1}', Contrasena='{2}'  WHERE id_administrador = '{3}'".format(usuario_string.get(), mail_string.get(), contra_string.get(), id_seleccionado)
				fcursor.execute(sql)
				basedatos.commit()
				messagebox.showinfo("Modificar","Administrador Modificado!!")
				id_cliente = -1
		guardar = "sin valor"
		cargar_tabla()
		estado_inicial_botones_cajas()
	def nuevo_btn():
		global guardar
		guardar = "nuevo"
		boton_nuevo.configure(state='disabled')
		boton_modificar.configure(state='disabled')
		boton_eliminar.configure(state='disabled')
		boton_guardar.configure(state='normal')
		boton_cancelar.configure(state='normal')

		entry_usuario.configure(state='normal')
		entry_mail.configure(state='normal')
		entry_contra.configure(state='normal')
		entry_contra_2.configure(state='normal')
	def filtros_consulta():
		if usuario_buscar.get() == "":
			messagebox.showerror("Error", "Debes ingresar al menos un dato")
			return
		else:
			own_bd = pymysql.connect(host="localhost", user="root", passwd="", db="sistema_gestion_libreria")
			fcursor = own_bd.cursor()
			print("no se rompio")
			fcursor.execute("SELECT * FROM Administradores WHERE Usuario = '"+str(usuario_buscar.get())+"'")
			for item in grid.get_children():
				grid.delete(item)
			for row in fcursor: 
				grid.insert("", 0, text=row[0],values=(row[1],row[2],row[3]))
			own_bd.close()
	def limpiar():
		cargar_tabla()
		usuario_buscar.set("")
	ventana_admins.title("Administradores")
	ventana_admins.iconbitmap("Imágenes/logoProA.ico")

	boton_nuevo = Button(ventana_admins, text="Nuevo", width=15, height=1,bg="#0A0AF0", state=NORMAL, fg="white", command=(nuevo_btn))
	boton_nuevo.pack
	boton_nuevo.place(x=10,y=10)

	boton_modificar = Button(ventana_admins, text="Modificar", width=15, height=1,bg="#0A0AF0", state=NORMAL, fg="white", command=modificar_btn)
	boton_modificar.pack
	boton_modificar.place(x=130,y=10)

	boton_eliminar = Button(ventana_admins, text="Eliminar", width=15, height=1,bg="#FF1F24", fg="white", command=eliminar_cliente)
	boton_eliminar.pack
	boton_eliminar.place(x=250,y=10)

	boton_guardar = Button(ventana_admins, text="Guardar", width=15, height=1,bg="#5ab507", state=DISABLED, fg="white", command=(guardar_admin))
	boton_guardar.pack
	boton_guardar.place(x=370,y=10)

	boton_cancelar = Button(ventana_admins, text="Cancelar", width=15, height=1,bg="#FF1F24", fg="white", command=estado_inicial_botones_cajas)
	boton_cancelar.pack
	boton_cancelar.place(x=490,y=10)

	boton_salir = Button(ventana_admins, text="Salir", width=10, height=1,bg="#FF1F24", fg="white", command=(lambda: cross("menuLargo", ventana_admins)))
	boton_salir.pack
	boton_salir.place(x=610,y=10)

	grid = ttk.Treeview(ventana_admins, columns=("col1","col2", "col3"))

	grid.column("#0", width=50, anchor=CENTER)
	grid.column("col1", width=150, anchor=CENTER)
	grid.column("col2", width=150, anchor=CENTER)
	grid.column("col3", width=150, anchor=CENTER)

	grid.heading("#0", text="Id", anchor=CENTER)
	grid.heading("col1", text="Usuario", anchor=CENTER)
	grid.heading("col2", text="Mail", anchor=CENTER)
	grid.heading("col3", text="Contraseña", anchor=CENTER)

	grid.pack()
	grid.place(x=20, y=130, width=650, height=450)

	label_entry = Label(ventana_admins, text="ID")
	label_entry.pack()
	label_entry.place(x=10,y=50)

	id_string = StringVar()
	entry_id = Entry(ventana_admins, state=DISABLED, textvariable=id_string)
	entry_id.pack()
	entry_id.place(x=10, y=75)

	label_entry = Label(ventana_admins, text="Usuario")
	label_entry.pack()
	label_entry.place(x=140,y=50)

	usuario_string = StringVar()
	entry_usuario = Entry(ventana_admins, textvariable=usuario_string, state=DISABLED)
	entry_usuario.pack()
	entry_usuario.place(x=140, y=75)

	label_entry = Label(ventana_admins, text="Mail")
	label_entry.pack()
	label_entry.place(x=270,y=50)

	mail_string = StringVar()
	entry_mail = Entry(ventana_admins, textvariable=mail_string, state=DISABLED)
	entry_mail.pack()
	entry_mail.place(x=270, y=75)

	label_entry = Label(ventana_admins, text="Contraseña")
	label_entry.pack()
	label_entry.place(x=420,y=50)

	contra_string = StringVar()
	entry_contra = Entry(ventana_admins, textvariable=contra_string, state=DISABLED)
	entry_contra.pack()
	entry_contra.place(x=420, y=75)

	label_entry = Label(ventana_admins, text="Repetir contraseña")
	label_entry.pack()
	label_entry.place(x=550,y=50)

	contra_string_2 = StringVar()
	entry_contra_2 = Entry(ventana_admins, textvariable=contra_string_2, state=DISABLED)
	entry_contra_2.pack()
	entry_contra_2.place(x=550,y=75)



	framee = ttk.Labelframe(ventana_admins, width=350, height=80, text="Buscar")
	framee.pack()
	framee.place(x=170 ,y=580)

	label_frame1 = Label(ventana_admins, text="Usuario")
	label_frame1.pack()
	label_frame1.place(x=190 ,y=598)

	usuario_buscar = StringVar()
	entry_buscar_user = Entry(ventana_admins, textvariable=usuario_buscar)
	entry_buscar_user.pack()
	entry_buscar_user.place(x=190, y=620)

	button_buscar = Button(ventana_admins, text="Filtrar", width=8, height=2, bg="#0A0AF0", fg="white", command=filtros_consulta)
	button_limpiar = Button(ventana_admins, text="Limpiar", width=8, height=2, bg="#0A0AF0", fg="white", command=limpiar)
	button_buscar.pack()
	button_limpiar.pack()
	button_buscar.place(x=350 ,y=600)
	button_limpiar.place(x=420 , y=600)
	cargar_tabla()
	mainloop()
def ventana_alquileres_fun(): #Creamos la quinta ventana menu estudiantes
	global ventana_alquileres
	ventana_alquileres=Tk()

	#-------está porción de código va a centrar mi ventana---------
	w = 1210
	h = 600
	ws = ventana_alquileres.winfo_screenwidth()
	hs = ventana_alquileres.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_alquileres.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------

	
	LabelFrame( ventana_alquileres, width= 410, height=120).place(x=5,y=10)

	#coso
	imagen_net = Image.open("Imágenes/login.png")
	resize = imagen_net.resize((100,100))
	imagen_net = ImageTk.PhotoImage(resize)
	label_net=Label(ventana_alquileres, image=imagen_net)
	label_net.pack()
	label_net.place(x=10, y=15)
	
	Label(ventana_alquileres, text="DNI").place(x=120, y=20)
	Label(ventana_alquileres, text="Apellido").place(x=120, y=45)
	Label(ventana_alquileres, text="Nombre").place(x=120, y=70)
	Label(ventana_alquileres, text="Socio").place(x=120, y=95)
	dni = StringVar()
	apellido = "------------------------"
	nombre = "------------------------"
	socio = "------------------------"
	entry_dni=Entry(ventana_alquileres,textvariable= dni, state='disabled')
	entry_dni.pack()
	entry_dni.place(x=190,y=20)

	Label(ventana_alquileres, text=apellido).place(x=190, y=45)
	Label(ventana_alquileres, text=nombre).place(x=190, y=70)
	Label(ventana_alquileres, text=socio).place(x=190, y=95)

	btn_buscar = Button(ventana_alquileres,text="Buscar",width="10",bg="navy", fg="white")
	btn_buscar.pack()
	btn_buscar.place(x=325,y=17)






	
	LabelFrame( ventana_alquileres, width= 410, height=120).place(x=425,y=10)
	imagen_net2 = Image.open("Imágenes/portada.png")
	resize2 = imagen_net2.resize((100,100))
	imagen_net2 = ImageTk.PhotoImage(resize2)
	label_net=Label(ventana_alquileres, image=imagen_net2)
	label_net.pack()
	label_net.place(x=430, y=15)
	
	Label(ventana_alquileres, text="Codigo").place(x=540, y=20)
	Label(ventana_alquileres, text="Titulo").place(x=540, y=45)
	Label(ventana_alquileres, text="Autor").place(x=540, y=70)
	Label(ventana_alquileres, text="Genero").place(x=540, y=95)
	codigo = StringVar()
	titulo = "------------------------"
	autor = "------------------------"
	genero = "------------------------"
	entry_dni=Entry(ventana_alquileres,textvariable= dni, state='disabled')
	entry_dni.pack()
	entry_dni.place(x=610,y=20)

	Label(ventana_alquileres, text=titulo).place(x=610, y=45)
	Label(ventana_alquileres, text=autor).place(x=610, y=70)
	Label(ventana_alquileres, text=genero).place(x=610, y=95)

	btn_buscar = Button(ventana_alquileres,text="Buscar",width="10",bg="navy", fg="white")
	btn_buscar.pack()
	btn_buscar.place(x=745,y=17)



	btn_buscar = Button(ventana_alquileres,text="Nuevo Prestamo",width="20",bg="navy", fg="white")
	btn_buscar.pack()
	btn_buscar.place(x=840,y=10)
	btn_buscar = Button(ventana_alquileres,text="Guardar Prestamo",width="20",bg="green", fg="white")
	btn_buscar.pack()
	btn_buscar.place(x=840,y=40)
	btn_buscar = Button(ventana_alquileres,text="Cancelar Prestamo",width="20",bg="red", fg="white")
	btn_buscar.pack()
	btn_buscar.place(x=840,y=70)
	btn_buscar = Button(ventana_alquileres,text="Salir",width="20",bg="navy", fg="white", command=(lambda: cross("menuLargo", ventana_alquileres)))
	btn_buscar.pack()
	btn_buscar.place(x=840,y=100)

	grid = ttk.Treeview(ventana_alquileres, columns=("col1", "col2", "col3","col4", "col5", "col6", "col7", "col8", "col9")) #from tkinter import ttk
	
	grid.column("#0", width=50)
	grid.column("col1", width=80, anchor=CENTER)
	grid.column("col2", width=100, anchor=CENTER)
	grid.column("col3", width=100, anchor=CENTER)
	grid.column("col4", width=70, anchor=CENTER)
	grid.column("col5", width=150, anchor=CENTER)
	grid.column("col6", width=100, anchor=CENTER)
	grid.column("col7", width=80, anchor=CENTER)
	grid.column("col8", width=80, anchor=CENTER)
	grid.column("col9", width=80, anchor=CENTER)
	
	grid.heading("#0", text="Id")
	grid.heading("col1", text="DNI", anchor=CENTER)
	grid.heading("col2", text="Apellido", anchor=CENTER)
	grid.heading("col3", text="Nombre", anchor=CENTER)
	grid.heading("col4", text="Codigo", anchor=CENTER)
	grid.heading("col5", text="Titulo", anchor=CENTER)
	grid.heading("col6", text="Autor", anchor=CENTER)
	grid.heading("col7", text="Inicio", anchor=CENTER)
	grid.heading("col8", text="Fin", anchor=CENTER)
	grid.heading("col9", text="Estado", anchor=CENTER)
	
	grid.pack()
	grid.place(x=5,y=130, width=985, height=350)
	grid['selectmode']='browse'#Modifica el tipo de selección

	LabelFrame( ventana_alquileres, width= 410, height=120).place(x=1000,y=10)


	calendario1 = Calendar(ventana_alquileres)
	calendario1.pack()
	calendario1.place(x=1000, y=10, width=200, height=200)

	calendario2 = Calendar(ventana_alquileres)
	calendario2.pack()
	calendario2.place(x=1000, y=220 , width=200, height=200)

	mainloop()

def ventana_verificar_admin():
	global ventana_verificar
	global sesion_iniciada
	print(sesion_iniciada)
	ventana_verificar=Tk()
	#-------está porción de código centrara mi ventana---------
	w = 300
	h = 300
	ws = ventana_verificar.winfo_screenwidth()
	hs = ventana_verificar.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana_verificar.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana_verificar.title("Ingresar al Sistema")
	ventana_verificar.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es

	def verificador():
		if contrasena.get() == sesion_iniciada[1]:
			cross("admins", ventana_verificar)
		else:
			messagebox.showerror("Error", "Contraseña incorrecta")
			cross("menuLargo", ventana_verificar)
	#------------------------------------------------------
	#abrimos la imagen
	imagen2 = Image.open("Imágenes/candado.png")
	#cambiamos el tamaño
	resized2 = imagen2.resize((100, 100))
	imagen2 = ImageTk.PhotoImage(resized2)
	Label(ventana_verificar,image=imagen2).place(x=100,y=10)
	#-----------------------------------------------------

	text = "Verifíque su identidad ingresando la contraseña de su usuario" + "a"
	Label(ventana_verificar, text="Verifíque su identidad ingresando \n la contraseña de su usuario", font=("Arial", 11)).place(x=45, y=125)
	
	contrasena = StringVar()
	entry_contrasena = Entry(ventana_verificar, textvariable=contrasena, show="•")
	entry_contrasena.pack()
	entry_contrasena.place(x=90, y=180)

	Button(ventana_verificar,text="Continuar", height="1", width="20",bg="navy", fg="white", font=("Calibri", 15), command=verificador).place(x=45,y=220)
	mainloop()
opciones = {"alquileres": ventana_alquileres_fun, "verificador": ventana_verificar_admin, "admins": administradores_ventana, "libros": libros_ventana_fun, "login": ventana_login_fun, "menuLargo": ventana_menu_principal_fun, "menuCorto": ventana_menu_fun, "clientes": ventana_clientes_fun}
def cross(abrir, cerrar):
	abrirPag = opciones.get(abrir)
	cerrar.destroy()
	abrirPag()
#ventana_principal_fun()
ventana_login_fun()
#libros_ventana_fun()