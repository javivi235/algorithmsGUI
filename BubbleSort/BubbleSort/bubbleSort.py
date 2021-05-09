import time 


def bubbleSort(data, dibujar, cnv):
    cnv.create_text(100,200,text="Inciando bubble sort...") 
    for _ in range(len(data)-1): 
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                
                cnv.delete("all") 
                a = (("El numero " + str(data[j]) + " es mayor que " + str(data[j+1])))
                cnv.create_text(100,100,text=a)
                 
                
                data[j],data[j+1] = data[j+1], data[j] 
                b = (("Intercambiando de lugar " + str(data[j]) + " con " + str(data[j+1])))
                cnv.create_text(100,120,text=b)

                dibujar(data, 
                    [
                    'green' 
                    if x == j or x  == j+1 
                    else 'red' for x in range(len(data))
                    ]
                )
                time.sleep(2)
    dibujar(data, ['green' for x in range(len(data))])
    
    cnv.delete("all")
    cnv.create_text(100,200,text="Array ordenado con Bubble Sort")
