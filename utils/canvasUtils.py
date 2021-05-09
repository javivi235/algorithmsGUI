from tkinter import * 
from tkinter import ttk 

class HashTableSlot:
    def __init__(self,canvas,x1,y1,x2,y2,valor):
        self.canvas = canvas
        self.imagen = canvas.create_rectangle(x1,y1,x2,y2)
        val = str(valor)
        aux_x = int((x1+x2)/2)
        aux_y = int((y1+y2)/2)
        self.text =  canvas.create_text(aux_x,aux_y,text=valor)

x1_slot = 75
x2_slot = 175
y1_slot = 50
y2_slot = 100
offset_y_slots = int((y2_slot - y1_slot)*1.5)

def dibujar_slots_tabla_hash(canvas,m):
    canvas.delete("all")
    for i in range(0,m):
        rect = HashTableSlot(canvas,x1_slot,y1_slot+offset_y_slots*i,x2_slot,y2_slot+offset_y_slots*i,i)

def hash_div_aux(m,k):
    return k % m


inicio_flecha_hash = 20
final_flecha_hash =  50
largo_flecha = final_flecha_hash - inicio_flecha_hash
alto_keys = 30
largo_keys = 60
offset_x_keys = int(largo_keys*1.5)

def dibujar_keys_tabla_hash(canvas,m,slots):
    canvas.delete("all")
    dibujar_slots_tabla_hash(canvas,m)
    for slot in slots.keys():
        if slots[slot]:
            y1_key =  (offset_y_slots + offset_y_slots*slot) -alto_keys/2
            y2_key =  (offset_y_slots + offset_y_slots*slot) + alto_keys/2
            flecha_offset =  inicio_flecha_hash + final_flecha_hash
            for i in range(len(slots[slot])): 
                x1 = x2_slot+ flecha_offset + (flecha_offset + largo_keys) * i 
                x2 = x2_slot+ flecha_offset + largo_keys + (flecha_offset + largo_keys) * i  
                x1_flecha = x2_slot + inicio_flecha_hash + (flecha_offset + largo_keys) * i
                x2_flecha = x2_slot + inicio_flecha_hash + largo_flecha + (flecha_offset + largo_keys) * i
                canvas.create_line(x1_flecha, offset_y_slots + offset_y_slots*slot,x2_flecha, offset_y_slots + offset_y_slots*slot, arrow=LAST)  
                rect = HashTableSlot(canvas, x1, y1_key ,x2, y2_key , slots[slot][i])



