import time 
from tkinter import * 
from tkinter import ttk 
from config import default 

config = default 

def bubbleSort(data, dibujar, lista, tk, canvas):
    print("entro a bubble sort")

    lista.insert(lista.index('end'),"Inciando bubble sort....")

    for _ in range(len(data)-1): 
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                                
                a = (("El numero " + str(data[j]) + " es mayor que " + str(data[j+1])))
                lista.insert(lista.index('end'), str(a))
                
                data[j],data[j+1] = data[j+1], data[j] 
                b = (("Intercambiando de lugar " + str(data[j]) + " con " + str(data[j+1])))
                lista.insert(lista.index('end'), str(b))

                dibujar(data, 
                    [
                    config["color_yellow"] 
                    if x == j or x  == j+1 
                    else config["color_white"] for x in range(len(data))
                    ]
                )
                tk.after(500, None)
                canvas.update()

    dibujar(data, [config["color_green"] for x in range(len(data))])
    
    lista.insert(lista.index('end'), 'Ordenado')
    