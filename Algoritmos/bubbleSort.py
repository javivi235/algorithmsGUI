import time 

data = []

def bubbleSort(data, dibujar, lista):
    print("entro a bubble sort")

    lista.insert(2,"Inciando bubble sort....")

    for _ in range(len(data)-1): 
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                
                lista.delete(0, 'end')
                
                a = (("El numero " + str(data[j]) + " es mayor que " + str(data[j+1])))
                lista.insert(5, str(a))
                
                 
                
                data[j],data[j+1] = data[j+1], data[j] 
                b = (("Intercambiando de lugar " + str(data[j]) + " con " + str(data[j+1])))
                lista.insert(6, str(b))

                dibujar(data, 
                    [
                    'yellow' 
                    if x == j or x  == j+1 
                    else 'white' for x in range(len(data))
                    ]
                )
                time.sleep(2)
    dibujar(data, ['green' for x in range(len(data))])
    
    lista.delete(0, 'end')
    lista.insert(7, "Ordenado")
    