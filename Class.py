import tkinter as tk
from tkinter import ttk
from datetime import *

class Class():
    def __init__(self):
        self.lista={}

    def criarLista(self,array):
        for i in range(len(array)):
            nome=array[i]
            posicao=i+1
            self.lista.update({nome:posicao})

    def criarListaAno(self,array):
        for i in range(len(array)):
            nome=array[i]
            posicao=array[i]
            self.lista.update({nome:posicao})

    def getLista(self):
        return self.lista

    def inputDia(self):
        self.dia=[]
        for i in range (1,32):
            if i<10:
                self.dia.append("0"+str(i))
            else:
                self.dia.append(str(i))

        self.criarLista(self.dia)
    def printDia(self):
        return self.dia

    def inputMes(self):
        #mes=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
        mes=["01","02","03","04","05","06","07","08","09","10","11","12"]
        self.criarLista(mes)
        return mes
    def inputAno(self):
        ano=["2019","2020","2021","2022","2023"]
        self.criarListaAno(ano)
        return ano

'''lista=Class()

root = tk.Tk()
lista.inputDia()
lista.inputMes()
lista.inputAno()
root.mainloop()'''

