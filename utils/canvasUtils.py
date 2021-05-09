from tkinter import *
from tkinter import ttk
sys.path.append('..')
from Algoritmos.arbolAVL import ArbolAVL

r = 30

def drawAVLTree(avlTree, canvas):

    if avlTree is None:
        return
    x = int(int(canvas["width"])/2)

    while x/(2**avlTree.altura) < r:
        x *= 2

    drawAVLTreeRecursive(avlTree, x, r + 10, canvas, int(x/2), avlTree.altura, r+10)

def drawAVLTreeRecursive(avlTree, x, y, canvas, d, altura, dy):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1)
    canvas.create_text(int((x0 + x1)/2), int((y0+y1)/2), text=str(avlTree.value))

    deltaX = (d/(2**altura)) * (2**avlTree.altura)

    if avlTree.arbolIzq is not None:
        canvas.create_line(x-r, y, x-deltaX, y+dy)
        drawAVLTreeRecursive(avlTree.arbolIzq, x-deltaX, y+dy+r, canvas, d, altura, dy)

    if avlTree.arbolDer is not None:
        canvas.create_line(x+r, y, x+deltaX, y+dy)
        drawAVLTreeRecursive(avlTree.arbolDer, x+deltaX, y+dy+r, canvas, d, altura, dy)
