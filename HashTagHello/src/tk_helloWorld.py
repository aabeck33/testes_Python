from tkinter import *
from tkinter import ttk

def multiplica():
    m = 2*4
    texto_resultado['text'] = m
    

janela = Tk()
janela.geometry('400x400')

janela.title('Isso é um teste')
texto_orientacao = Label(janela, text='Clique no botão')
texto_orientacao.grid(column=0, row=0)

texto_orientacao = Label(janela, text='')
texto_orientacao.grid(column=0, row=1)

texto_orientacao = Label(janela, text='_____________________')
texto_orientacao.grid(column=1, row=0)

texto_orientacao = Label(janela, text='Outra linha')
texto_orientacao.grid(column=0, row=2)

botao = Button(janela, text='Resultado', command=multiplica)
botao.grid(column=1, row=2)

texto_resultado = Label(janela, text='')
texto_resultado.grid(column=0, row=4, padx=10, pady=10)

janela.mainloop()