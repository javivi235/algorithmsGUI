import time 
from tkinter import * 
from tkinter import ttk 

from config import default 

config = default


def mergeSort(data, dibujar, lista2, tk, canvas):
    mergeSortAlg(data, 0, len(data)-1, dibujar, lista2, tk,canvas)
    
def mergeSortAlg(data, izq, der, dibujar, lista2, tk, canvas):
    
    if izq < der:
        medio = (izq + der) // 2
        
        mergeSortAlg(data, izq, medio, dibujar, lista2,tk,canvas) 
        mergeSortAlg(data, medio+1, der, dibujar, lista2,tk,canvas) 
        merge(data, izq, medio, der, dibujar, lista2,tk,canvas)

    

def merge(data, izq, medio, der, dibujar, lista2, tk,canvas):
    
    ladoIzq = data[izq:medio+1]
    
    ladoDer = data[medio+1:der+1]
    
    izqIdx = derIdx = 0 

    txt = ("Valor del medio: " + str(data[medio]))
    lista2.insert(lista2.index("end"), str(txt))
    

    text1 = ("Izquierda: " + str(ladoIzq))
    lista2.insert(lista2.index("end"), str(text1))

    text2= ("Derecha: " + str(ladoDer)) 
    lista2.insert(lista2.index("end"), str(text2))

    dibujar(data, getColorArray(len(data), izq, medio, der, lista2, tk,canvas))
    tk.after(500, None)
    canvas.update()

    

    for dataIdx in range(izq, der+1):

        if izqIdx < len(ladoIzq) and derIdx < len(ladoDer): 
            
            if ladoIzq[izqIdx] <= ladoDer[derIdx]:

                data[dataIdx] = ladoIzq[izqIdx] 
                izqIdx += 1
                
            else:
                data[dataIdx] = ladoDer[derIdx]
                derIdx += 1 
                
        elif izqIdx < len(ladoIzq):

            data[dataIdx] = ladoIzq[izqIdx]
            izqIdx += 1 

        else: 
            data[dataIdx] = ladoDer[derIdx]
            derIdx += 1 

    dibujar(data, [config["color_green"] if x >= izq and x <= der else "white" for x in range(len(data))])

    tk.after(1000, None)
    canvas.update()

def getColorArray(length, izq, medio, der, lista2, tk,canvas): 
    colorArray = []

    for i in range(length): 
        if i >= izq and i <= der: 
            if i >= izq and i <= medio:
                colorArray.append(config["color_yellow"])

            else:
                colorArray.append("pink")

        else:
            colorArray.append(config["color_white"])

    
    return colorArray