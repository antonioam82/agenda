from tkinter import*
from tkinter import messagebox

def guardar():
    print("Hola")

def eliminar():
    print("Hola")

def iniciarArchivo():
    archivo=open("ag.txt","a")
    archivo.close()

def cargar():
    archivo=open("ag.txt","r")
    linea=archivo.readline()
    if linea:
        while linea:
            if linea[-1]=="\n":
                linea=linea[:-1]
            lista.append(linea)
            linea=archivo.readline()
    archivo.close()

def escribirContacto():
    archivo=open("ag.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+"\n")
    archivo.close()

def consultar():
    r=Text(ventana,width=80,height=15)
    lista.sort()
    valores=[]
    r.insert(INSERT,"Nombre\t\tApellido P\t\tApellido M\t\tTelefono\t\tCorreo\n")
    for elemento in lista:
        arreglo=elemento.split("$")
        valores.append(arreglo[3])
        
    
    
cargar()
lista=[]
ventana=Tk()
nombre=StringVar()
app=StringVar()
apm=StringVar()
telefono=StringVar()
correo=StringVar()
conteeliminar=StringVar()
color_fondo="dodger blue"
color_letra="#FFF"
color_boton="DodgerBlue4"
ventana.title("Agenda con archivos")
ventana.geometry("700x500")
ventana.configure(background=color_fondo)
etiquetatitulo=Label(ventana,text="Agenda con archivos",bg=color_fondo,fg=color_letra,font=("Helvetica",16)).place(x=255,y=10)
etiquetaN=Label(ventana,text="Nombre: ",bg=color_fondo,fg=color_letra).place(x=50,y=50)
cajaN=Entry(ventana,textvariable=nombre).place(x=150,y=50)
etiquetaAPP=Label(ventana,text="Apellido paterno: ",bg=color_fondo,fg=color_letra).place(x=50,y=80)
cajaAPP=Entry(ventana,textvariable=app).place(x=150,y=80)
etiquetaAPM=Label(ventana,text="Apellido materno: ",bg=color_fondo,fg=color_letra).place(x=50,y=110)
cajaAPM=Entry(ventana,textvariable=apm).place(x=150,y=110)
etiquetaT=Label(ventana,text="Telefono: ",bg=color_fondo,fg=color_letra).place(x=50,y=140)
cajaT=Entry(ventana,textvariable=telefono).place(x=150,y=140)
etiquetaC=Label(ventana,text="Correo: ",bg=color_fondo,fg=color_letra).place(x=50,y=170)
cajaC=Entry(ventana,textvariable=correo).place(x=150,y=170)
etiquetaEliminar=Label(ventana,text="Telefono: ",bg=color_fondo,fg=color_letra).place(x=370,y=50)
SpinTel=Spinbox(ventana,textvariable=conteeliminar).place(x=450,y=50)
botonG=Button(ventana,text="Guardar",command=guardar,bg=color_boton,fg="white").place(x=180,y=200)
botonEl=Button(ventana,text="Eliminar",command=eliminar,bg=color_boton,fg="white").place(x=470,y=80)


ventana.mainloop()
