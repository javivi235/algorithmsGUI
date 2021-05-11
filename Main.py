from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import sys

sys.path.append('..')

from Algoritmos.arbolAVL import ArbolAVL
from Algoritmos.ArbolRN import ArbolRN
from Algoritmos.TablaHash import TablaHash
from Algoritmos.bubbleSort import bubbleSort
from Algoritmos.mergeSort import mergeSort

from config import default
from utils.canvasUtils import *

config = default
tk = Tk()
tk.title('Proyecto Final')
tk.geometry(f'{config["reference_width"] + 30}x{config["reference_height"]+230}')
tk.wm_maxsize(config["reference_width"] + 30, config["reference_height"]+230)
tk.config(bg = 'white')

arbolAVL = None
arbolRN  = None
tablaHash = None

data = []

def dibujar(data, color):
    canvas.delete("all") 
    cHeight = 600
    cWidth = 600 
    
    algoWidth = cHeight /  (len(data) + 1)
    algoHeight = cWidth /  (len(data) + 1)
    offset = 20
    spacing = 10

    tamData = [i / max(data) for i in data]

    for i, height in enumerate(tamData):
        
        x0 = (i) * algoWidth + offset + spacing
        y0 = (cHeight // 2) - 25

        
        x1 = (i+1) * algoWidth + offset
        y1 = (cHeight // 2) + 25

        canvas.create_rectangle(x0,y0,x1,y1, fill = color[i])
        canvas.create_text(x0+2,y0, anchor = SW, text=str(data[i]))

    
    tk.update_idletasks()

def ordenar_elementos():
    print("Iniciando algoritmo")
    global data 
    
    if algoritmos_box.get() == 'Bubble Sort':
        bubbleSort(data, dibujar, list_box_results,tk, canvas)

    elif algoritmos_box.get() == 'Merge Sort':
        mergeSort(data, dibujar, list_box_results, tk, canvas)

    dibujar(data, [config['color_green'] for x in range(len(data))])
    

def insertar_elemento():
    if validarInput(input_valor.get()):
        entrada = int(input_valor.get())
        if algoritmos_box.get() == "Bubble Sort":
            data.append(entrada)
            dibujar(data, [config['color_red'] for x in range(len(data))])

        elif algoritmos_box.get() == "Merge Sort":
            data.append(entrada)
            dibujar(data, [config['color_red'] for x in range(len(data))])

        elif algoritmos_box.get() == "Tabla Hash":
            global tablaHash
            print("Insertar Tabla Hash " + input_valor.get())
            if tablaHash is None:
                messagebox.showinfo(message="Primero debe inicializar la tabla hash fijando un valor de m", title="Advertencia")
            else:
                tablaHash.insertar(canvas,entrada)
                for paso in tablaHash.pasos:
                    list_box_results.insert(list_box_results.index("end") + 1, f'{paso}')

        elif algoritmos_box.get() == "Árbol AVL":
            global arbolAVL
            canvas.delete("all")
            print("Insertar Árbol AVL " + input_valor.get())
            if arbolAVL is None:
                arbolAVL = ArbolAVL(None, None, int(input_valor.get()), None, list_box_results)
                list_box_results.insert(list_box_results.index("end") + 1, f'Agregamos la raiz {input_valor.get()} ')
            else:
                arbolAVL.insertar(input_valor.get())

            dibujar_arbol(arbolAVL, "avl", canvas)
                
        elif algoritmos_box.get() == "Árbol Rojo y Negro":
            global arbolRN
            canvas.delete("all")
            print("Insertar Árbol Rojo y Negro " + input_valor.get())
            if arbolRN is None:
                arbolRN = ArbolRN()
                arbolRN.insertar(int(input_valor.get()))
                list_box_results.insert(list_box_results.index("end") + 1, f'Agregamos la raiz {input_valor.get()} ')
            else:
                arbolRN.insertar(int(input_valor.get()))
                for paso in arbolRN.pasos:
                    list_box_results.insert(list_box_results.index("end") + 1, f'{paso}')
            
            dibujar_arbol(arbolRN, "rojo-negro", canvas)

    else:
        messagebox.showerror("Error", "Por favor ingrese un valor numérico")

    input_valor.delete(0, END)

def borrar_elemento():
    if validarInput(input_valor.get()):
        entrada = int(input_valor.get())
        if algoritmos_box.get() == "Bubble Sort":
            print("Borrar Bubble Sort " + input_valor.get())
        elif algoritmos_box.get() == "Merge Sort":
            print("Borrar Merge Sort " + input_valor.get())
        elif algoritmos_box.get() == "Tabla Hash":
            global tablaHash
            print("Borrar Tabla Hash " + input_valor.get())
            if tablaHash is None:
                messagebox.showinfo(message="Primero debe inicializar la tabla hash fijando un valor de m", title="Advertencia")
            else:
                tablaHash.borrar(canvas,entrada)
                for paso in tablaHash.pasos:
                    list_box_results.insert(list_box_results.index("end") + 1, f'{paso}')

        elif algoritmos_box.get() == "Árbol AVL":
            global arbolAVL
            canvas.delete("all")
            print("Borrar Árbol AVL " + input_valor.get())
            if arbolAVL is None:
                messagebox.showerror("Error", "No se puede borrar un elemento de un árbol vacío")
            else:
                arbolAVL.delete(int(input_valor.get()))
            dibujar_arbol(arbolAVL, "avl", canvas)

        elif algoritmos_box.get() == "Árbol Rojo y Negro":
            global arbolRN
            canvas.delete("all")

            print("Borrar Árbol Rojo y Negro " + input_valor.get())
            if arbolRN is None:
                messagebox.showerror("Error", "No se puede borrar un elemento de un árbol vacío")
            else:
                arbolRN.borrar(int(input_valor.get()))
                for paso in arbolRN.pasos:
                    list_box_results.insert(list_box_results.index("end") + 1, f'{paso}')
            dibujar_arbol(arbolRN, "rojo-negro", canvas)

    else:
        messagebox.showerror("Error", "Por favor ingrese un valor numérico")
    return

def guardar_m():
    global tablaHash
    if validarInput(input_m.get()): 
        entrada = abs(int(input_m.get()))
        if tablaHash is None:
            tablaHash = TablaHash(entrada)
            tablaHash.crear_tabla(canvas)
        else:
            tablaHash.m = entrada
            tablaHash.crear_tabla(canvas)
    else:
        messagebox.showerror("Error", "Por favor ingrese un valor numérico")

def limpiar():
    global arbolAVL,arbolRN,tablaHash
    arbolAVL = None
    arbolRN  = None
    tablaHash = None
    canvas.delete("all")
    list_box_results.delete(0, END)

    if algoritmos_box.get() == 'Bubble Sort':
        global data
        data = []

    elif algoritmos_box.get() == 'Merge Sort':
        data = []
        

tool_bar_frame = Frame(tk, width = config["reference_width"], height = int(config["reference_height"]/7)*2, bg = config["color_bg_general"] )
tool_bar_frame.grid(row = 0, column = 0, sticky=W)

label_algoritmo = Label(tool_bar_frame, text='Algoritmo ', font = config["fuente_titulo"], borderwidth=1, bg = config["color_bg_general"] , fg = config["color_letra_general"])
label_algoritmo.grid(row=0,column=0,sticky = W,padx = 5, pady = 5)


label_valor = Label(tool_bar_frame, text='Valor', font = config["fuente_titulo"], borderwidth=1, bg = config["color_bg_general"] , fg = config["color_letra_general"])
label_valor.grid(row=0,column=2,padx = 5, pady = 5, sticky = W)

input_valor = Entry(tool_bar_frame)
input_valor.grid(row=0,column=3, padx = 5, pady = 5, sticky = W)

boton_insertar = Button(tool_bar_frame, text = 'Insertar', font= config["fuente_fields"], command = insertar_elemento, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
boton_insertar.grid(row = 0, column = 4, padx = 5, pady = 5, sticky = W)

boton_borrar = Button(tool_bar_frame, text = 'Borrar', font= config["fuente_fields"] ,command = borrar_elemento, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
boton_borrar.grid(row = 0, column = 5,  padx = 5, pady = 5, sticky = W)

boton_limpiar = Button(tool_bar_frame, text = 'Limpiar', font= config["fuente_fields"] ,command = limpiar, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
boton_limpiar.grid(row = 0, column = 6,  padx = 5, pady = 5, sticky = W)

label_m = Label(tool_bar_frame, text='Valor de M', font = config["fuente_titulo"], borderwidth=1, bg = config["color_bg_general"] , fg = config["color_letra_general"])
input_m = Entry(tool_bar_frame)
boton_m = Button(tool_bar_frame, text = 'Fijar M', command = guardar_m, font=config["fuente_fields"], bg = config["color_bg_botones"], fg = config["color_letra_botones"])

boton_ordenar = Button(tool_bar_frame, text = 'Ordenar', command = ordenar_elementos, font=config["fuente_fields"], bg = config["color_bg_botones"], fg = config["color_letra_botones"])
boton_ordenar.grid(row = 0, column = 10, padx = 5, pady = 5, sticky = W)    

algoritmo_actual = StringVar()
algoritmos_box = ttk.Combobox(tool_bar_frame, textvariable = algoritmo_actual,font = config["fuente_fields"],values=['Bubble Sort', 'Merge Sort', 'Tabla Hash', 'Árbol AVL', 'Árbol Rojo y Negro'], state="readonly")
algoritmos_box.grid(row=0, column=1, padx = 5, pady = 5)
algoritmos_box.current(0)

def validarInput(valor):
    entrada = "X"
    try:
        entrada =  int(valor)
    except:
        return False
    return True        

def modified (event) :
    data = [] 
    limpiar()
    if(algoritmos_box.get() == "Tabla Hash"):
        label_m.grid(row = 0,column = 7,padx = 5, pady = 5, sticky = W)
        input_m.grid(row = 0,column = 8, padx = 5, pady = 5, sticky = W)
        boton_m.grid(row = 0, column = 9, sticky = W)
        boton_ordenar.grid_forget()

    elif(algoritmos_box.get() == 'Bubble Sort' or algoritmos_box.get() == 'Merge Sort'):
        boton_ordenar.grid(row = 0, column = 10, padx = 5, pady = 5, sticky = W)    
        label_m.grid_forget()
        input_m.grid_forget()
        boton_m.grid_forget()

    else:
        label_m.grid_forget()
        input_m.grid_forget()
        boton_m.grid_forget()
        boton_ordenar.grid_forget()

algoritmos_box.bind('<<ComboboxSelected>>', modified)

second_row_frame= Frame(tk, width = int(config["reference_width"]) - 100, bg = "green")
second_row_frame.grid(row = 1, column = 0, sticky="EWNS")

second_row_frame.columnconfigure(0, weight=3)
second_row_frame.columnconfigure(1, weight=1)


results_frame = Frame(second_row_frame, bg = "white")
results_frame.grid(row = 0, column = 0, sticky="EW")

canvas_x_scroll = Scrollbar(results_frame, orient="horizontal")
canvas_x_scroll.grid(row = 1, column = 0, sticky="EW")

canvas_y_scroll = Scrollbar(results_frame)
canvas_y_scroll.grid(row = 0, column = 1, sticky="NS")

canvas = Canvas(results_frame, width = int((config["reference_width"]-100)/4)*3, height =  int((config["reference_width"]-100)/5)*4-15, bg = config["color_bg_canvas"], scrollregion=(0,0,10000,10000))

canvas.grid(column=0, row=0, sticky="EW")

scrollbar_sentences_y = Scrollbar(tk, width=15)
scrollbar_sentences_y.grid(column=1, row=1, sticky="ENS")

list_box_results = Listbox(second_row_frame, width=40, font = config["fuente_fields"], bg = config["color_bg_botones"] , fg = config["color_letra_botones"], yscrollcommand=scrollbar_sentences_y.set)
list_box_results.grid(column=1, row=0, sticky="WENS")

canvas_x_scroll.config(command=canvas.xview)
canvas_y_scroll.config(command=canvas.yview)
canvas.config(xscrollcommand=canvas_x_scroll.set, yscrollcommand=canvas_y_scroll.set)
scrollbar_sentences_y.config(command=list_box_results.yview)

tk.mainloop()