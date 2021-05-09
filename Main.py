from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
import random 
from bubbleSort import bubbleSort

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
tk.geometry("1200x700")
# tk.maxsize(valores_globales["window_width"], valores_globales["window_height"])
tk.config(bg = 'white')

def insertar_elemento():
    if validarInput():
        if algoritmos_box.get() == "Bubble Sort":
            print("Bubble Sort " + input_valor.get())
        elif algoritmos_box.get() == "Merge Sort":
            print("Merge Sort " + input_valor.get())
        elif algoritmos_box.get() == "Tabla Hash":
            print("Tabla Hash " + input_valor.get())
        elif algoritmos_box.get() == "Árbol AVL":
            print("Árbol AVL " + input_valor.get())
        elif algoritmos_box.get() == "Árbol Rojo y Negro":
            print("Árbol Rojo y Negro " + input_valor.get())
    else:
        messagebox.showerror("Error", "Ingrese un valor numerico")

def borrar_elemento():
    return
def limpiar_canvas():
    return
def guardar_m():
    return
def escribir_resultado():
    return

tool_bar_frame = Frame(tk, width = valores_globales["window_width"], height = int(valores_globales["window_height"]/7)*2, bg = valores_globales["color_bg_general"] )
tool_bar_frame.grid(row = 0, column = 0, padx=10, pady=5, sticky=W)

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
        print("Añadiendo: " + str(entrada))        
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
second_row_frame= Frame(tk, width = int(valores_globales["window_width"]), height = int(valores_globales["window_height"]/2)*7, bg = "green" )
second_row_frame.grid(row = 1, column = 0)

results_frame = Frame(second_row_frame, width = int(valores_globales["window_width"]/2), height = int(valores_globales["window_height"]/2)*7, bg = "black" )
results_frame.grid(row = 0, column = 0)

sentencias_frame = Frame(second_row_frame, width = int(valores_globales["window_width"]/2), height = int(valores_globales["window_height"]/2)*7, bg = "red" )
sentencias_frame.grid(row = 0, column = 1)

canvas = Canvas(results_frame,width = int(valores_globales["window_width"]/4)*3, height = 100 , bg = valores_globales["color_bg_canvas"])
# # canvas.create_oval(105,105,105,105, fill = "yellow")
canvas.grid(row=0,column=0)

list_box_results = Listbox(sentencias_frame, width = 100, height = 100,font = valores_globales["fuente_fields"], bg = valores_globales["color_bg_botones"] , fg = valores_globales["color_letra_botones"])
list_box_results.grid(row=0,column=0)

tk.mainloop()