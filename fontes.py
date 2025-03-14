import tkinter as tk
import tkinter.font as tkFont 

root = tk.Tk()
fontes_disponiveis = []
fontes_disponiveis = tkFont.families()

for fonte in sorted (fontes_disponiveis):
    palavra = "produtos"
    palavra = fonte
    print(fonte)

