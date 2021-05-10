import time 

def mergeSort(data, dibujar, lista2):
    mergeSortAlg(data, 0, len(data)-1, dibujar, lista2)

def mergeSortAlg(data, izq, der, dibujar, lista2):
    
    if izq < der:
        medio = (izq + der) // 2
        
        mergeSortAlg(data, izq, medio, dibujar, lista2) 
        mergeSortAlg(data, medio+1, der, dibujar, lista2) 
        merge(data, izq, medio, der, dibujar, lista2)

    

def merge(data, izq, medio, der, dibujar, lista2):
    
    lista2.delete(0, 'end')
    
    dibujar(data, getColorArray(len(data), izq, medio, der))
    time.sleep(2)

    ladoIzq = data[izq:medio+1]
    
    ladoDer = data[medio+1:der+1]
    
    izqIdx = derIdx = 0 

    txt = ("Valor del medio: " + str(data[medio]))
    lista2.insert(4, str(txt))

    text1 = ("Izquierda: " + str(ladoIzq))
    lista2.insert(5, str(text1))

    text2= ("Derecha: " + str(ladoDer)) 
    lista2.insert(6, str(text2))

    for dataIdx in range(izq, der+1):

        if izqIdx < len(ladoIzq) and derIdx < len(ladoDer): 
            
            txt3 = ("Realizando cambio") 
            if ladoIzq[izqIdx] <= ladoDer[derIdx]:

                lista2.insert(7, str(txt3))
                data[dataIdx] = ladoIzq[izqIdx] 
                izqIdx += 1
                
            else:
                lista2.insert(7, str(txt3))
                data[dataIdx] = ladoDer[derIdx]
                derIdx += 1 
                
        elif izqIdx < len(ladoIzq):

            lista2.insert(7, str(txt3))
            data[dataIdx] = ladoIzq[izqIdx]
            izqIdx += 1 

        else: 
            lista2.insert(7, str(txt3))
            data[dataIdx] = ladoDer[derIdx]
            derIdx += 1 

    dibujar(data, ["green" if x >= izq and x <= der else "white" for x in range(len(data))])

    time.sleep(2)


def getColorArray(length, izq, medio, der): 
    colorArray = []

    for i in range(length): 
        if i >= izq and i <= der: 
            if i >= izq and i <= medio:
                colorArray.append("yellow")

            else:
                colorArray.append("pink")

        else:
            colorArray.append("white")

    return colorArray
