import time 

def bubbleSort(data, dibujar):
    for _ in range(len(data)-1): 
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]
                dibujar(data, 
                    [
                    'green' 
                    if x == j or x  == j+1 
                    else 'red' for x in range(len(data))
                    ]
                )
                time.sleep(1)
    dibujar(data, ['green' for x in range(len(data))])

    