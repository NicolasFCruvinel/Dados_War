from random import randrange
from turtle import clear
import PySimpleGUI as sg
import os

def dados(atacante, defensor):
    a, b, = [], []
    vd, va = 0, 0
    for i in range(atacante):
        a.append(randrange (1, 7))
    for j in range(defensor):
        b.append(randrange (1, 7))

    a.sort(reverse=True)
    b.sort(reverse=True)

    for k in range(min(len(a),len(b))):
        if a[k]<=b[k]:
            vd += 1

    va = (min(len(a),len(b))) - vd
    print("\n" * os.get_terminal_size().lines)
    print ('Dados do ataque:',a)
    print ('Dados da defesa:',b)
    #print (a, " o/a atacante e ", b, " para o/a defensor(a)")
    print("")
    print ('Atacante perde:',vd)
    print ('Defensor(a) perde:',va)

sg.theme('Reddit')
layout = [
    [sg.Text('Ataque:')],
    [sg.Input(key="at", size=(15,2))],
    [sg.Text('Defesa:')],
    [sg.Input(key="df", size=(15,2))],
    [sg.Button('Guerrear')],
    [sg.Output(size=(30,7))]
]

janela = sg.Window('War', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Guerrear':
        dados(int(valores['at']), int(valores['df']))