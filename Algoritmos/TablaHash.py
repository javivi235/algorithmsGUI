class TablaHash:
    def __init__(self,m):
        self.m = m
        self.slots = None
        self.pasos = list()

    def crear_tabla(self):
        slots = dict()
        self.pasos = list()
        self.pasos.append("Inicializando una tabla hash con m = " + str(self.m))
        for i in range(self.m):
            slots[i] = list()
        self.slots = None
        self.slots = slots

    def hash_div(self,k):
        return k % self.m
    
    def insertar(self,k):
        self.pasos = list()
        hash_value = self.hash_div(k)
        self.pasos.append("Insertar " + str(k))
        self.pasos.append("El hash calculado para " + str(k) + " es " + str(hash_value))
        if  k in self.slots[hash_value]:
            self.pasos.append("El elemento " + str(k)+ " ya está en la tabla")
            return
        self.slots[hash_value].append(k)
        self.slots[hash_value].sort()

    def borrar(self,k):
        self.pasos = list()
        hash_value = self.hash_div(k)
        self.pasos.append("Eliminar " + str(k))
        self.pasos.append("El hash calculado para " + str(k) + " es " + str(hash_value))
        if  k not in self.slots[hash_value]:
            self.pasos.append("El elemento " + str(k)+ " no está en la tabla")
            return
        self.slots[hash_value].remove(k)


# tabla = TablaHash(17)
# tabla.crear_tabla()
# print(tabla.pasos)
# tabla.insertar(10)
# tabla.insertar(35)

# tabla.insertar(1)
# tabla.insertar(18)
# tabla.insertar(52)
# tabla.insertar(1)

# tabla.insertar(127)


# tabla.borrar(52)
# tabla.borrar(52)

# print(tabla.slots.values())
# print(tabla.pasos)