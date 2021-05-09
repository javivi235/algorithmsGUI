from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import random
import os
import sys

sys.path.append('..')

from Algoritmos.arbolAVL import ArbolAVL

from BubbleSort.BubbleSort.bubbleSort import bubbleSort

valores_globales = {
    "fuente_titulo" : ("Inter",15),
    "fuente_fields": ("Inter",12),
    "color_bg_general": "white",
    "color_letra_general": "black",
    "color_letra_botones": "white",
    "color_bg_botones": "#455054",
    "color_input": "gray",
    "color_bg_canvas": "#F5F5DC",
    "window_width" : 1200,
    "window_height" : 700,

}

tk = Tk()
tk.title('Proyecto Final')
tk.geometry("1200x1005")
# tk.maxsize(valores_globales["window_width"], valores_globales["window_height"])
tk.config(bg = 'white')

arbolAVL = None

def insertar_elemento():
    if validarInput():
        if algoritmos_box.get() == "Bubble Sort":
            print("Bubble Sort " + input_valor.get())
        elif algoritmos_box.get() == "Merge Sort":
            print("Merge Sort " + input_valor.get())
        elif algoritmos_box.get() == "Tabla Hash":
            print("Tabla Hash " + input_valor.get())
        elif algoritmos_box.get() == "Árbol AVL":
            global arbolAVL
            print("Árbol AVL " + input_valor.get())
            if arbolAVL is None:
                arbolAVL = ArbolAVL(None, None, input_valor.get(), None, list_box_results)
                list_box_results.insert(list_box_results.index("end") + 1, f'Agregamos la raiz {input_valor.get()} ')

            else:
                arbolAVL.insertar(input_valor.get())

        elif algoritmos_box.get() == "Árbol Rojo y Negro":
            print("Árbol Rojo y Negro " + input_valor.get())
    else:
        messagebox.showerror("Error", "Ingrese un valor numerico")

def borrar_elemento():
    if validarInput():
        if algoritmos_box.get() == "Bubble Sort":
            print("Bubble Sort " + input_valor.get())
        elif algoritmos_box.get() == "Merge Sort":
            print("Merge Sort " + input_valor.get())
        elif algoritmos_box.get() == "Tabla Hash":
            print("Tabla Hash " + input_valor.get())
        elif algoritmos_box.get() == "Árbol AVL":
            global arbolAVL
            print("Árbol AVL " + input_valor.get())
            if arbolAVL is None:
                list_box_results.insert(list_box_results.index("end"), f'No se puede borrar { input_valor.get()}')
            else:
                arbolAVL.delete(input_valor.get())
                print(arbolAVL)

        elif algoritmos_box.get() == "Árbol Rojo y Negro":
            print("Árbol Rojo y Negro " + input_valor.get())
    else:
        messagebox.showerror("Error", "Ingrese un valor numerico")
    return
def limpiar_canvas():
    return
def guardar_m():
    return
def escribir_resultado():
    return

#general_frame = Frame(tk, bg="yellow")
#general_frame.grid(sticky="NS")

tool_bar_frame = Frame(tk, width = valores_globales["window_width"], height = int(valores_globales["window_height"]/7)*2, bg = valores_globales["color_bg_general"] )
tool_bar_frame.grid(row = 0, column = 0, sticky=W)

label_algoritmo = Label(tool_bar_frame, text='Algoritmo ', font = valores_globales["fuente_titulo"], borderwidth=1, bg = valores_globales["color_bg_general"] , fg = valores_globales["color_letra_general"])
label_algoritmo.grid(row=0,column=0,sticky = W,padx = 5, pady = 5)


label_valor = Label(tool_bar_frame, text='Valor', font = valores_globales["fuente_titulo"], borderwidth=1, bg = valores_globales["color_bg_general"] , fg = valores_globales["color_letra_general"])
label_valor.grid(row=0,column=2,padx = 5, pady = 5, sticky = W)

input_valor = Entry(tool_bar_frame)
input_valor.grid(row=0,column=3, padx = 5, pady = 5, sticky = W)

boton_insertar = Button(tool_bar_frame, text = 'Insertar', font= valores_globales["fuente_fields"], command = insertar_elemento, bg = valores_globales["color_bg_botones"], fg=valores_globales["color_letra_botones"])
boton_insertar.grid(row = 0, column = 4, padx = 5, pady = 5, sticky = W)

boton_borrar = Button(tool_bar_frame, text = 'Borrar', font= valores_globales["fuente_fields"] ,command = borrar_elemento, bg = valores_globales["color_bg_botones"], fg=valores_globales["color_letra_botones"])
boton_borrar.grid(row = 0, column = 5,  padx = 5, pady = 5, sticky = W)

boton_limpiar = Button(tool_bar_frame, text = 'Limpiar', font= valores_globales["fuente_fields"] ,command = limpiar_canvas, bg = valores_globales["color_bg_botones"], fg=valores_globales["color_letra_botones"])
boton_limpiar.grid(row = 0, column = 6,  padx = 5, pady = 5, sticky = W)

label_m = Label(tool_bar_frame, text='Valor de M', font = valores_globales["fuente_titulo"], borderwidth=1, bg = valores_globales["color_bg_general"] , fg = valores_globales["color_letra_general"])
input_m = Entry(tool_bar_frame)
boton_m = Button(tool_bar_frame, text = 'Fijar M', command = guardar_m, font=valores_globales["fuente_fields"], bg = valores_globales["color_bg_botones"], fg = valores_globales["color_letra_botones"])

algoritmo_actual = StringVar()
algoritmos_box = ttk.Combobox(tool_bar_frame, textvariable = algoritmo_actual,font = valores_globales["fuente_fields"],values=['Bubble Sort', 'Merge Sort', 'Tabla Hash', 'Árbol AVL', 'Árbol Rojo y Negro'])
algoritmos_box.grid(row=0, column=1,padx = 5, pady = 5)
algoritmos_box.current(0)


def validarInput():
    entrada = "X"
    try:
        entrada =  int(input_valor.get())
        #print("Añadiendo: " + str(entrada))
    except:
        return False
    return True        

def modified (event) :
    if(algoritmos_box.get() == "Tabla Hash"):
        label_m.grid(row = 0,column = 7,padx = 5, pady = 5, sticky = W)
        input_m.grid(row = 0,column = 8, padx = 5, pady = 5, sticky = W)
        boton_m.grid(row = 0, column = 9, sticky = W)
    else:
        label_m.grid_forget()
        input_m.grid_forget()
        boton_m.grid_forget()

algoritmos_box.bind('<<ComboboxSelected>>', modified)

#Seccion del canvas y del listbox
second_row_frame= Frame(tk, width = int(valores_globales["window_width"]), bg = "green")
second_row_frame.grid(row = 1, column = 0, sticky="EWNS")

second_row_frame.columnconfigure(0, weight=3)
second_row_frame.columnconfigure(1, weight=1)

# width = int(valores_globales["window_width"]/2), height = int(valores_globales["window_height"]/2)*7,

#results_frame = Frame(second_row_frame, bg = "black" )
#results_frame.grid(row = 0, column = 0, sticky="NE")

#width = int(valores_globales["window_width"]/2), height = int(valores_globales["window_height"]/2)*7,
#sentencias_frame = Frame(second_row_frame, bg = "red")
#sentencias_frame.grid(row = 0, column = 1)

#width = int(valores_globales["window_width"]/4)*3, height =  int(valores_globales["window_width"]/7)*5 ,
canvas = Canvas(second_row_frame, width = int(valores_globales["window_width"]/4)*3, height =  int(valores_globales["window_width"]/5)*4, bg = valores_globales["color_bg_canvas"])
#canvas.create_oval(0,0,105,105, fill = "black")
canvas.grid(column=0,row=0, sticky="EW")

scrollbar_sentences_y = Scrollbar(tk, width=15)
scrollbar_sentences_y.grid(column=1,row=1, sticky="ENS")

#width = 100, height = 100,
list_box_results = Listbox(second_row_frame, width=30, font = valores_globales["fuente_fields"], bg = valores_globales["color_bg_botones"] , fg = valores_globales["color_letra_botones"], yscrollcommand=scrollbar_sentences_y.set)
list_box_results.grid(column=1, row=0, sticky="WENS")

scrollbar_sentences_y.config(command=list_box_results.yview)

tk.mainloop()