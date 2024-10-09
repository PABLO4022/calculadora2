from tkinter import *
from tkinter import ttk

cor1 = '#070807'  # preto
cor2 = '#f2fff2'  # branco
cor3 = '#322e61'  # azul
cor4 = '#5a5c61'  # cinza
cor5 = '#de871d'  # laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x320')
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=55, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()
valor_texto.set(todos_valores)

def entrar_valores(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except:
        valor_texto.set('Erro')
        todos_valores = ''

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

app_label = Label(frame_tela,
                  textvariable=valor_texto,
                  width=16,
                  height=2,
                  padx=7,
                  relief=FLAT,
                  anchor='e',
                  justify=RIGHT,
                  font=('ivy 16'),
                  bg=cor3,
                  fg=cor2)
app_label.place(x=0, y=0)

buttons = [
    ('C', limpar_tela, 0, 0),
    ('%', lambda: entrar_valores('%'), 118, 0),
    ('/', lambda: entrar_valores('/'), 177, 0),
    ('7', lambda: entrar_valores('7'), 0, 52),
    ('8', lambda: entrar_valores('8'), 59, 52),
    ('9', lambda: entrar_valores('9'), 118, 52),
    ('*', lambda: entrar_valores('*'), 177, 52),
    ('4', lambda: entrar_valores('4'), 0, 104),
    ('5', lambda: entrar_valores('5'), 59, 104),
    ('6', lambda: entrar_valores('6'), 118, 104),
    ('-', lambda: entrar_valores('-'), 177, 104),
    ('1', lambda: entrar_valores('1'), 0, 156),
    ('2', lambda: entrar_valores('2'), 59, 156),
    ('3', lambda: entrar_valores('3'), 118, 156),
    ('+', lambda: entrar_valores('+'), 177, 156),
    ('0', lambda: entrar_valores('0'), 0, 208),
    ('.', lambda: entrar_valores('.'), 118, 208),
    ('=', calcular, 177, 208)
]

for (text, command, x, y) in buttons:
    Button(frame_corpo,
           command=command,
           text=text,
           width=5 if text != '0' else 11,
           height=2,
           bg=cor4 if text not in ('/', '*', '-', '+', '=') else cor5,
           fg=cor2 if text not in ('/', '*', '-', '+', '=') else cor2,
           font=('ivy 13 bold'),
           relief=RAISED,
           overrelief=RIDGE).place(x=x, y=y)

janela.mainloop()
