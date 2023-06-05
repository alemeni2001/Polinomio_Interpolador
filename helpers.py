import os
import math

WIDTH = 70
LEFTMARGIN = 2
SYMBOL = '@'

def cls():
    # Verificar el sistema operativo y ejecutar el comando correspondiente para limpiar la pantalla
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def prLn(size, **kwargs):
    up = int(kwargs['up']) if 'up' in kwargs else 0
    dw = int(kwargs['dw']) if 'dw' in kwargs else 0
    lf = bool(kwargs['lf']) if 'lf' in kwargs else False
    
    for _ in range(up):
        print("\n", end="")
    lftMg() if lf else ""
    for _ in range(size):
        print(f"{SYMBOL}", end="")
    for _ in range(dw):
        print("\n", end="")

def prTxt(txt, **kwargs):
    up = int(kwargs['up']) if 'up' in kwargs else 0
    dw = int(kwargs['dw']) if 'dw' in kwargs else 0
    lf = bool(kwargs['lf']) if 'lf' in kwargs else False
    col = int(kwargs['col']) if 'col' in kwargs else 3
    
    le = len(txt)
    free = WIDTH - len(txt) - col*2
    left = math.floor(free/2)
    right = left if (free%2 == 0) else left+1
    txt_spaced = prSpc(left) + txt + prSpc(right)
   
    prLn(col,lf=lf)
    print(f"{txt_spaced}", end="")
    prLn(col)    

def lftMg():
    for _ in range(LEFTMARGIN):
        print("\t", end="")

def prSpc(size) -> str:
    whiteSpace = ""
    for _ in range(size):
        whiteSpace += " "
    return whiteSpace
 
