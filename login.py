import PySimpleGUI as sg



Layout = [
    [sg.Text  ('usuário')],
    [sg.Input(key = 'usuario')],
    [sg.Text('Senha')],
    [sg.Input(key = 'senha')],
    [sg.Button('login')],
    [sg.Button('Cadastro')],
    [sg.Text('',key = 'mensagem')],
        
    
    ]
window =  sg.Window('tela de login',layout=Layout) 


while True:
    
    event , values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'login':
        usuario_correto = 'marcos'
        senha_correta = '123'
    
        usuario = values['usuario']
        senha = values['senha']

    if senha == senha_correta and usuario == usuario_correto:
        window['mensagem'].update('login feito com sucesso, isso e so um teste ')
        
    else:
        window['mensagem'].update('login errado pf coloca as credencias ja salvas no codigo fonte(isso e so um teste)')


