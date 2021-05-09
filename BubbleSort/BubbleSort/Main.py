from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
from bubbleSort import bubbleSort
from mergeSort import mergeSort

variable_globales = {

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
    "algoritmos_box_width": 900,
    "algoritmos_box_height": 200,
    "canvas_width": 600,
    "canvas_height": 380,


}

tk = Tk()
tk.title('Examen Final')
#tk.maxsize(900, 600)
tk.config(bg = variable_globales["color_bg_general"])

algoritmo = StringVar()
data = []

def dibujar(data, color):
    c.delete("all") 
    cHeight = 380
    cWidth = 600 
    
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

def ordenar_elementos():
    print("Se selecciono: " + algoritmo.get())
    print("Iniciando algoritmo")

    global data 
    
    if algoritmos_box.get() == 'MERGE SORT':
        mergeSort(data, dibujar, c2)

    elif algoritmos_box.get() == 'BUBBLE SORT':
        bubbleSort(data, dibujar, c2)

    elif algoritmos_box.get() == 'HASH TABLES':
        pass 

    elif algoritmos_box.get() == 'ARBOL AVL':
        pass 

    elif algoritmos_box.get() == 'ARBOLES ROJO Y NEGRO':
        pass 

    dibujar(data, ['green' for x in range(len(data))])

def agregar_elemento():
    global data 
    
    input =  int(input_valor.get())
    input_valor.delete(0, END)

    try: 
        
        print("valor input:")
        print(input)
        
        data.append((input)) 
        print(str(data))

        dibujar(data, ['red' for x in range(len(data))])
        
    except:
        messagebox.showerror("Error", "Ingrese un valor numerico")

def limpiar_canvas():
    global data 
    data = []
    c.delete("all") 
    print(data)

def borrar():
    pass 

def guardar_m():
    pass 

tool_bar_frame = Frame(tk, width = variable_globales["algoritmos_box_width"], height = variable_globales["algoritmos_box_height"], bg = variable_globales["color_bg_general"] )
tool_bar_frame.grid(row = 0, column = 0, padx=10, pady=5)

c = Canvas(tk, width = variable_globales["canvas_width"], height = variable_globales["canvas_height"],  borderwidth = 1, bg = variable_globales["color_bg_canvas"])
c.grid(row = 1, column = 0, padx=10, pady=5, sticky = W)

c2 = Canvas(tk, width = variable_globales["canvas_width"], height = variable_globales["canvas_height"],  borderwidth = 1, bg = 'grey')
c2.grid(row = 1, column = 1, padx=10, pady=5, sticky = W)

label = Label(tool_bar_frame, text='Algoritmo: ', font = variable_globales["fuente_titulo"], borderwidth=1, fg = 'black')
label.grid(row=0,column=0,  padx=5, pady=5, sticky = W)

algoritmos_box = ttk.Combobox(tool_bar_frame, textvariable = algoritmo, values=['BUBBLE SORT', 'MERGE SORT', 'HASH TABLES', 'ARBOL AVL', 'ARBOLES ROJO Y NEGRO'])
algoritmos_box.grid(row=0, column=1, padx=5, pady=5)
algoritmos_box.current(0)

botonStart = Button(tool_bar_frame, text = 'Ordenar', command = ordenar_elementos, bg = variable_globales["color_bg_botones"], fg = variable_globales["color_letra_botones"])
botonStart.grid(row = 0, column = 2, padx = 5, pady = 5)

label_valor = Label(tool_bar_frame, text='Valor: ', font = variable_globales["fuente_titulo"],  borderwidth=1 , fg = 'black')
label_valor.grid(row=0,column=3, padx = 5, pady = 5, sticky = W)

input_valor = Entry(tool_bar_frame)
input_valor.grid(row=0,column=6, padx = 5, pady = 5, sticky = W)

label_m = Label(tool_bar_frame, text='Valor de M', font = variable_globales["fuente_titulo"], borderwidth=1, bg = variable_globales["color_bg_general"] , fg = variable_globales["color_letra_general"])
input_m = Entry(tool_bar_frame)

boton_m = Button(tool_bar_frame, text = 'Fijar M', command = guardar_m(), font=variable_globales["fuente_fields"], bg = variable_globales["color_bg_botones"], fg = variable_globales["color_letra_botones"])


boton_insertar = Button(tool_bar_frame, text = 'Insertar', command = agregar_elemento, bg = variable_globales["color_bg_botones"], fg = variable_globales["color_letra_botones"])
boton_insertar.grid(row = 0, column = 7,  padx = 5, pady = 5, sticky = W)

boton_borrar = Button(tool_bar_frame, text = "Borrar", command =borrar, bg = variable_globales["color_bg_botones"], fg = variable_globales["color_letra_botones"])
boton_borrar.grid(row = 0, column = 8,  padx = 5, pady = 5, sticky = W)

boton_limpiar = Button(tool_bar_frame, text = 'Limpiar', command = limpiar_canvas, bg = variable_globales["color_bg_botones"], fg = variable_globales["color_letra_botones"])
boton_limpiar.grid(row = 0, column = 9,  padx = 5, pady = 5, sticky = W)

def modified(evet):
    if(algoritmos_box.get() == "HASH TABLES"):
        label_m.grid(row = 0,column = 10,padx = 5, pady = 5, sticky = W)
        input_m.grid(row = 0,column = 11, padx = 5, pady = 5, sticky = W)
        boton_m.grid(row = 0, column = 12, sticky = W)

    else: 
        label_m.grid_forget()
        input_m.grid_forget()
        boton_m.grid_forget()

algoritmos_box.bind('<<ComboboxSelected>>', modified)

tk.mainloop()
