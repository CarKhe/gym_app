import tkinter as tk
from tkinter import ttk
import time
import datetime
from PIL import Image,ImageTk
from tkcalendar import DateEntry



class MenuPrincipal:
    def __init__(self,titulo,dimensiones):
        ventana = tk.Tk()
        ventana.title(titulo) 
        ventana.geometry(dimensiones)
        ventana.iconbitmap("img/ico.ico")
        ventana.resizable(False,False)
        
        barra_menu = tk.Menu(ventana)
        ventana.config(menu=barra_menu)

        barra_menu.add_command(label="Inicio")
        

        cliente = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Cliente",menu=cliente)
        cliente.add_command(label="Renovar Sub.", command=self.vista_busqueda_resultado_1)
        cliente.add_separator()
        cliente.add_command(label="Nuevo",command=self.vista_crear)
        cliente.add_command(label="Buscar",command=self.vista_buscar)
        cliente.add_command(label="Modificar",command=self.vista_busqueda_resultado_0)
        
        planes = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Planes",menu=planes)
        planes.add_command(label="Nuevo",command= lambda:self.sin_busqueda_menu(ventana))
        planes.add_command(label="Buscar",command= lambda: self.cambio_busqueda_manual(ventana))
        planes.add_command(label="Modificar",command=lambda: self.pago_realizado(ventana))
        
        empleado = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Empleado",menu=empleado)
        empleado.add_command(label="Nuevo")
        empleado.add_command(label="Buscar")
        empleado.add_command(label="Modificar")   
        
        canvas = tk.Canvas(ventana,width=3,height=375,bg="black")
        canvas.place(relx=0.44)
        canvas.create_line(1,3,1,50, fill="black",width=6)
        
        reloj = tk.Label(ventana)
        reloj.config(fg="black",font=("Arial",20,"bold"))
        reloj.place(relx=0.85)
        
         

        
        
        fecha = tk.Label(ventana,text=datetime.datetime.now().strftime("%a %d-%b-%Y"))
        fecha.config(fg="black",font=("Arial",20,"bold"))
        fecha.place(relx=0.45)
        
        
        
        cliente = tk.Label(ventana,text="Cliente:")
        cliente.config(fg="black",font=("Arial",16,"bold"))
        cliente.place(relx=0.02,rely=0.035)
        
        entrada = tk.Entry(ventana)
        entrada.config(fg="black",font=("Arial",20),width=17)
        entrada.place(relx=0.02,rely=0.10 , width=280)
        entrada.focus()
        
        boton = tk.Button(ventana,text="Buscar")
        boton.config(fg="white",bg="green",height=2,width=4,border=2)
        boton.place(relx=0.375,rely=0.1,width=45,height=36)
        
        
        
        
        frame1 = tk.Frame(ventana)
        frame1.place(relx=0.02,rely=0.208,width=330,height=298)
        
        imagen_pil = Image.open("img/zoro.png").resize((120,120))
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        logo = tk.Label(frame1,image=imagen_tk)
        logo.place(relx=0.20,rely=0.22,anchor= "center")
        
        nombre = tk.Label(frame1,text="Nombre:")
        nombre.config(fg="black",font=("Arial",14,"bold"))
        nombre.place(relx=0.39,rely=0.015)
        
        nombre_completo = tk.Label(frame1,text="Carlos Rodriguez")
        nombre_completo.config(fg="black",font=("Arial",14))
        nombre_completo.place(relx=0.39,rely=0.11)
        
        suscripcion = tk.Label(frame1,text="Suscripción:")
        suscripcion.config(fg="black",font=("Arial",14,"bold"))
        suscripcion.place(relx=0.39,rely=0.22)
        
        tipo_suscripcion = tk.Label(frame1,text="Mensual")
        tipo_suscripcion.config(fg="black",font=("Arial",14))
        tipo_suscripcion.place(relx=0.39,rely=0.32)
        
        entrenador = tk.Label(frame1,text="Entrenador:")
        entrenador.config(fg="black",font=("Arial",14,"bold"))
        entrenador.place(relx=0.015,rely=0.45)
        
        nombre_entrenador = tk.Label(frame1,text="José Torres")
        nombre_entrenador.config(fg="black",font=("Arial",14))
        nombre_entrenador.place(relx=0.015,rely=0.55)
        
        fecha = tk.Label(frame1,text="Fecha de Pago:")
        fecha.config(fg="black",font=("Arial",14,"bold"))
        fecha.place(relx=0.5,rely=0.45)
        
        fecha_limite = tk.Label(frame1,text="24-02-24")
        fecha_limite.config(fg="black",font=("Arial",14))
        fecha_limite.place(relx=0.5,rely=0.55)
        
        mensaje_entrada = tk.Label(frame1,text="¡Acceso Concedido!")
        mensaje_entrada.config(fg="white",bg="Green",font=("Arial",24,"bold"))
        mensaje_entrada.place(relx=0.5,rely=0.8,anchor= "center")
        
        
        
        
        frame2 = tk.Frame(ventana,bg="#525252")
        frame2.place(relx=0.45,rely=0.1,width=435,height=340)
        
        grid = ttk.Treeview(frame2,columns=("col1", "col2", "col3", "col4"))
        
        grid.column("#0",width=40)
        grid.column("col1",width=100, anchor="center")
        grid.column("col2",width=90, anchor="center")
        grid.column("col3",width=90, anchor="center")
        grid.column("col4",width=100, anchor="center")
        
        grid.heading("#0",text="Id", anchor="center")
        grid.heading("col1",text="Foto", anchor="center")
        grid.heading("col2",text="Nombre", anchor="center")
        grid.heading("col3",text="Entrenador", anchor="center")
        grid.heading("col4",text="Hora-Entrada", anchor="center")
        
        
        grid.pack(side="left", fill="y",)
        
        scroll_bar = tk.Scrollbar(frame2, orient="vertical") 
        scroll_bar.pack( side = "right", fill = "y" ) 
        grid.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config( command = grid.yview ) 

        def actualizar_hora():
            reloj.config(text=time.strftime("%H:%M:%S"))
            ventana.after(1000,actualizar_hora)
        
        actualizar_hora()
        ventana.mainloop()
    
    def vista_crear(self):
        vetnana_toplevel = tk.Toplevel()
        vetnana_toplevel.title("Nuevo Cliente")
        vetnana_toplevel.iconbitmap("img/ico.ico")
        vetnana_toplevel.geometry("500x300")
        vetnana_toplevel.resizable(False,False)
        
        imagen_pil = Image.open("img/nami.jpg").resize((170,170))
        lunaWindowImage = ImageTk.PhotoImage(imagen_pil)
        lunaWindowLabel = tk.Label(vetnana_toplevel, image =lunaWindowImage , borderwidth=2, relief="solid")
        lunaWindowLabel.place(x=10,y=10)
        lunaWindowLabel.image = lunaWindowImage 
        
        
        boton = tk.Button(vetnana_toplevel,text="Cambiar Imagen")
        boton.config(fg="black",bg="gray",height=2,width=23)
        boton.place(x=11,y=190)
        
        nombre_txt = tk.Label(vetnana_toplevel,text="Nombre(s):")
        nombre_txt.config(fg="black",font=("Arial",14))
        nombre_txt.place(x=187,y=5)
        
        nombre = tk.Entry(vetnana_toplevel)
        nombre.config(fg="black",font=("Arial",14))
        nombre.place(x=190,y=35, width=290)
        nombre.focus()
        
        apellido_txt = tk.Label(vetnana_toplevel,text="Apellidos(s):")
        apellido_txt.config(fg="black",font=("Arial",14))
        apellido_txt.place(x=187,y=60)
        
        apellido = tk.Entry(vetnana_toplevel)
        apellido.config(fg="black",font=("Arial",14))
        apellido.place(x=190,y=90, width=290)

        
        fecha_nac_txt = tk.Label(vetnana_toplevel,text="Fecha Nac.:")
        fecha_nac_txt.config(fg="black",font=("Arial",14))
        fecha_nac_txt.place(x=187,y=120)
        
        data_entry = DateEntry(vetnana_toplevel,selectmode="day",date_pattern="dd-mm-y")
        data_entry.place(x=190,y=150, width=120,height=30)
        
        suscripcion_txt = tk.Label(vetnana_toplevel,text="Suscripción:")
        suscripcion_txt.config(fg="black",font=("Arial",14))
        suscripcion_txt.place(x=330,y=120)
        
        combobox = ttk.Combobox(vetnana_toplevel,font=("Arial",14))
        combobox.place(x=330,y=150,width=150)
        elementos = ["Planes","E2","E3"]
        combobox["values"] = elementos


        entrenador_txt = tk.Label(vetnana_toplevel,text="Entrenador:")
        entrenador_txt.config(fg="black",font=("Arial",14))
        entrenador_txt.place(x=190,y=195)
        
        combobox_entrenador = ttk.Combobox(vetnana_toplevel,font=("Arial",14))
        combobox_entrenador.place(x=330,y=195,width=150)
        entrenadores = ["Jose Torres","Julian","Elena"]
        combobox_entrenador["values"] = entrenadores
        
        guardar = tk.Button(vetnana_toplevel,text="Guardar")
        guardar.config(fg="white",bg="green",height=2,width=18)
        guardar.place(x=190,y=250)
        
        cancelar = tk.Button(vetnana_toplevel,text="Cancelar")
        cancelar.config(fg="white",bg="red",height=2,width=18)
        cancelar.place(x=330,y=250)
        
    def vista_buscar(self):
        vetnana_toplevel = tk.Toplevel()
        vetnana_toplevel.title("Buscar Cliente")
        vetnana_toplevel.iconbitmap("img/ico.ico")
        vetnana_toplevel.geometry("500x100")
        vetnana_toplevel.resizable(False,False)
        
        busqueda_txt = tk.Label(vetnana_toplevel,text="Buscar Cliente:")
        busqueda_txt.config(fg="black",font=("Arial",20))
        busqueda_txt.pack()
        
        busqueda = tk.Entry(vetnana_toplevel)
        busqueda.config(fg="black",font=("Arial",20))
        busqueda.place(width=300,x=250,y=55,anchor="center")
        busqueda.focus()
        
        buscar = tk.Button(vetnana_toplevel,text="Busc")
        buscar.config(fg="white",bg="blue",width=5,font=("Arial",13))
        buscar.place(x=400,y=37)
        
    
    def vista_busqueda_resultado_1(self):
        vetnana_toplevel = tk.Toplevel()
        vetnana_toplevel.title("Tajeta del Cliente")
        vetnana_toplevel.iconbitmap("img/ico.ico")
        vetnana_toplevel.geometry("500x230")
        vetnana_toplevel.resizable(False,False)
        
        imagen_pil = Image.open("img/nami.jpg").resize((170,170))
        lunaWindowImage = ImageTk.PhotoImage(imagen_pil)
        lunaWindowLabel = tk.Label(vetnana_toplevel, image =lunaWindowImage , borderwidth=2, relief="solid")
        lunaWindowLabel.place(x=10,y=10)
        lunaWindowLabel.image = lunaWindowImage 
        
        nombre_txt = tk.Label(vetnana_toplevel,text="Nombre(s):")
        nombre_txt.config(fg="black",font=("Arial",14))
        nombre_txt.place(x=187,y=5)
        
        nombre = tk.Label(vetnana_toplevel,text="Carlos Enrique")
        nombre.config(fg="black",font=("Arial",14),anchor="w", justify="left")
        nombre.place(x=190,y=35, width=290,)
        
        apellido_txt = tk.Label(vetnana_toplevel,text="Apellidos(s):")
        apellido_txt.config(fg="black",font=("Arial",14))
        apellido_txt.place(x=187,y=60)
        
        apellido = tk.Label(vetnana_toplevel,text="Rodriguez Moran")
        apellido.config(fg="black",font=("Arial",14),anchor="w", justify="left")
        apellido.place(x=190,y=90, width=290)

        
        fecha_nac_txt = tk.Label(vetnana_toplevel,text="Fecha Nac.:")
        fecha_nac_txt.config(fg="black",font=("Arial",14))
        fecha_nac_txt.place(x=187,y=120)
        
        data_entry = tk.Label(vetnana_toplevel,text="29-10-1999")
        data_entry.config(fg="black",font=("Arial",14))
        data_entry.place(x=190,y=150, width=120,height=30)
        
        suscripcion_txt = tk.Label(vetnana_toplevel,text="Suscripción:")
        suscripcion_txt.config(fg="black",font=("Arial",14))
        suscripcion_txt.place(x=330,y=120)
        
        combobox = tk.Label(vetnana_toplevel,text="1 mes entrenador")
        combobox.config(fg="black",font=("Arial",14))
        combobox.place(x=330,y=150,width=150)


        entrenador_txt = tk.Label(vetnana_toplevel,text="Entrenador:")
        entrenador_txt.config(fg="black",font=("Arial",14))
        entrenador_txt.place(x=10,y=195)
        
        combobox_entrenador = tk.Label(vetnana_toplevel,text="José Torres")
        combobox_entrenador.config(fg="black",font=("Arial",14))
        combobox_entrenador.place(x=110,y=195)
        
        fecha_pago_txt = tk.Label(vetnana_toplevel,text="Proximo Pago:")
        fecha_pago_txt.config(fg="black",font=("Arial",14))
        fecha_pago_txt.place(x=230,y=195)
        
        fecha_pago = tk.Label(vetnana_toplevel,text="24/02/2024")
        fecha_pago.config(fg="black",font=("Arial",14))
        fecha_pago.place(x=370,y=195)
        
    
    def vista_busqueda_resultado_0(self):
        vetnana_toplevel = tk.Toplevel()
        vetnana_toplevel.title("Cliente no encontrado")
        vetnana_toplevel.iconbitmap("img/ico.ico")
        vetnana_toplevel.geometry("500x230")
        vetnana_toplevel.resizable(False,False)
        
        imagen_pil = Image.open("img/negacion.png").resize((170,170))
        lunaWindowImage = ImageTk.PhotoImage(imagen_pil)
        lunaWindowLabel = tk.Label(vetnana_toplevel, image =lunaWindowImage , borderwidth=2, relief="solid")
        lunaWindowLabel.pack()
        lunaWindowLabel.image = lunaWindowImage 
        
        
    def cambio_busqueda_manual(self,ventana):
        
        frame1 = tk.Frame(ventana)
        frame1.place(relx=0.02,rely=0.208,width=330,height=298)
        
        grid = ttk.Treeview(frame1,columns=("col1", "col2", "col3"))
        
        grid.column("#0",width=4)
        grid.column("col1",width=100, anchor="center")
        grid.column("col2",width=100, anchor="center")
        grid.column("col3",width=100, anchor="center")
        
        grid.heading("#0",text="Id", anchor="center")
        grid.heading("col1",text="Nombre", anchor="center")
        grid.heading("col2",text="Fecha Pago", anchor="center")
        grid.heading("col3",text="Acceso", anchor="center")

        
        
        grid.pack(side="left", fill="y",)
        
        scroll_bar = tk.Scrollbar(frame1, orient="vertical") 
        scroll_bar.pack( side = "right", fill = "y" ) 
        grid.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config( command = grid.yview ) 
    
    def pago_realizado(self,ventana):
        frame1 = tk.Frame(ventana)
        frame1.place(relx=0.02,rely=0.208,width=330,height=298)
        
        imagen_pil = Image.open("img/zoro.png").resize((120,120))
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        logo = tk.Label(frame1,image=imagen_tk)
        logo.place(relx=0.20,rely=0.22,anchor= "center")
        logo.image = imagen_tk
        
        nombre = tk.Label(frame1,text="Nombre:")
        nombre.config(fg="black",font=("Arial",14,"bold"))
        nombre.place(relx=0.39,rely=0.015)
        
        nombre_completo = tk.Label(frame1,text="Carlos Rodriguez")
        nombre_completo.config(fg="black",font=("Arial",14))
        nombre_completo.place(relx=0.39,rely=0.11)
        
        suscripcion = tk.Label(frame1,text="Suscripción:")
        suscripcion.config(fg="black",font=("Arial",14,"bold"))
        suscripcion.place(relx=0.39,rely=0.22)
        
        tipo_suscripcion = tk.Label(frame1,text="Mensual")
        tipo_suscripcion.config(fg="black",font=("Arial",14))
        tipo_suscripcion.place(relx=0.39,rely=0.32)
        
        entrenador = tk.Label(frame1,text="Entrenador:")
        entrenador.config(fg="black",font=("Arial",14,"bold"))
        entrenador.place(relx=0.015,rely=0.45)
        
        nombre_entrenador = tk.Label(frame1,text="José Torres")
        nombre_entrenador.config(fg="black",font=("Arial",14))
        nombre_entrenador.place(relx=0.015,rely=0.55)
        
        fecha = tk.Label(frame1,text="Fecha de Pago:")
        fecha.config(fg="black",font=("Arial",14,"bold"))
        fecha.place(relx=0.5,rely=0.45)
        
        fecha_limite = tk.Label(frame1,text="24-02-24")
        fecha_limite.config(fg="black",font=("Arial",14))
        fecha_limite.place(relx=0.5,rely=0.55)
        
        mensaje_entrada = tk.Label(frame1,text="¡Acceso Concedido!")
        mensaje_entrada.config(fg="white",bg="Green",font=("Arial",24,"bold"))
        mensaje_entrada.place(relx=0.5,rely=0.8,anchor= "center")
    
    
    def sin_busqueda_menu(self,ventana):
        frame1 = tk.Frame(ventana,bg="#bfdaff")
        frame1.place(relx=0.02,rely=0.208,width=330,height=298)
        
        imagen_pil = Image.open("img/nami.jpg").resize((150,150))
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        logo = tk.Label(frame1,image=imagen_tk)
        logo.place(relx=0.5,rely=0.5,anchor= "center")  
        logo.image = imagen_tk
        
        
              
        

        



        
