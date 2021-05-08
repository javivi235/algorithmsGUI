from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import random 
from bubbleSort import bubbleSort

tk = Tk()
tk.title('Examen Final')
tk.maxsize(1500, 700)
tk.config(bg = 'black')

algoritmo = StringVar()
data = []

def dibujar(data, color):
    c.delete("all") 
    cHeight = 650
    cWidth = 700 

    
    algoWidth = cWidth /  (len(data) + 1)
    algoHeight = cWidth /  (len(data) + 1)
    offset = 20
    spacing = 10

    tamData = [i / max(data) for i in data]

    for i, height in enumerate(tamData):
        
        x0 = i * algoWidth + offset + spacing
        y0 = cHeight - height * 50

        
        x1 = (i+1) * algoWidth + offset
        y1 = cHeight 

        c.create_oval(x0,y0,x1,y1, fill = color[i])
        c.create_text(x0+2,y0, anchor = SW, text=str(data[i]))

    tk.update_idletasks()

def Ordenar():
    print("Se selecciono: " + algoritmo.get())
    print("Iniciando algoritmo")

    global data 
    bubbleSort(data, dibujar)

def agregar():
    global data 
    
    input =  int(inputVal.get())
    
    inputVal.delete(0, END)

    try: 

        print("valor input:")
        print(input)
        
        data.append((input)) 
        print(str(data))

        dibujar(data, ['red' for x in range(len(data))])
        
    except:
        messagebox.showerror("Error", "Ingrese un valor numerico")

def limpiar():
    global data 
    data = []
    c.delete("all") 
    print(data)
    
box = Frame(tk, width = 700, height = 500, bg = 'black' )
box.grid(row = 0, column = 0, padx=10, pady=5)
c = Canvas(tk, width = 700, height = 650,  bg = 'grey')
c.grid(row = 1, column = 0, padx=10, pady=5)

label = Label(box, text='Lista Algoritmos: ', font = ("Arial",15), borderwidth=1, bg = "black" , fg = 'white')
label.grid(row=0,column=0,  padx=5, pady=5, sticky = W)

menu = ttk.Combobox(box, textvariable = algoritmo, values=['BUBBLE SORT', 'MERGE SORT', 'HASH TABLES', 'ARBOL AVL', 'ARBOLES ROJO Y NEGRO'])
menu.grid(row=0, column=1, padx=5, pady=5)
menu.current(0)

botonStart = Button(box, text = 'Ordenar', command = Ordenar, bg = 'lime green')
botonStart.grid(row = 0, column = 2, padx = 5, pady = 5)

label = Label(box, text='Insertar valor: ', font = ("Arial",15), borderwidth=1, bg = "black" , fg = 'white')
label.grid(row=1,column=0, padx = 5, pady = 5, sticky = W)
inputVal = Entry(box)
inputVal.grid(row=1,column=1, padx = 5, pady = 5, sticky = W)

botonAdd = Button(box, text = 'Agregar', command = agregar, bg = 'lime green')
botonAdd.grid(row = 1, column = 2,  padx = 5, pady = 5, sticky = W)

botonClear = Button(box, text = 'Limpiar', command = limpiar, bg = 'lime green')
botonClear.grid(row = 1, column = 3,  padx = 5, pady = 5, sticky = W)

tk.mainloop()