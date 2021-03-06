#SE REQUIERE UN ARCHIVO DE TEXTO COMO EL "ag.txt" PRESENTE EN ESTE REPOSITORIO
from tkinter import*
from tkinter import messagebox

lista=[]

def guardar():
    n=nombre.get()
    ap=app.get()
    am=apm.get()
    c=correo.get()
    t=telefono.get()
    lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
    escribirContacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado en la egenda")
    nombre.set("")
    app.set("")
    apm.set("")
    correo.set("")
    telefono.set("")
    consultar()

def eliminar():
    eliminado=conteeliminar.get()
    removido=False
    for elemento in lista:
        arreglo=elemento.split("$")
        if conteeliminar.get()==arreglo[3]:
            lista.remove(elemento)
            removido=True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+eliminado)

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
    r.insert(INSERT,"Nombre\tApellido P\t\tApellido M\t\tTelefono\t\tCorreo\n")
    for elemento in lista:
        arreglo=elemento.split("$")
        valores.append(arreglo[3])
        r.insert(INSERT,arreglo[0]+"\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=230)
    spinTelefono=Spinbox(ventana,value=(valores),textvariable=conteeliminar).place(x=450,y=50)
    if lista==[]:
        spinTelefono=Spinbox(ventana,value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)
    


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
