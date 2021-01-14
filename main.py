from PySimpleGUI import PySimpleGUI as sg

layout = [
    [sg.Text("User"), sg.Input(key='user', size=(20, 1))],
    [sg.Text("Senha"), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar?')],
    [sg.Button('Ok'), sg.Button('Sair')]
]

window = sg.Window('Telao', layout, margins=(100, 50))

while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
        break
    if eventos == 'Ok':
        if valores['user'] == 'arthur' and valores['senha'] == '123':
            print('Bem vindo arthur')
        else:
            print('Usúario não identificado!')  