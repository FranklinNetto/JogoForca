import PySimpleGUI as sg

class JanelaJogo:

    def __init__(self):
        # Layout
        sg.theme('DarkBlue2')
        layout = [  
                    [sg.Text('Bem vindo ao Jogo de Forca!!!')],
                    [sg.Text('Escolha uma categoria uma das categorias para iniciar:')],
                    [sg.Radio('Frutas','opcao', default=True, key='frutas'), sg.Radio('Países','opcao',key='paises'),
                      sg.Radio('Objetos','opcao', key='objetos')],
                    [sg.Button('Ok'), sg.Button('Cancel')],
                    [sg.Output(size=(30, 20))]
                ]

        # Janela

        self.janela = sg.Window('Jogo da Forca', layout)

               

        #window.close()
        # Dados da tela

    def Iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break        
            frutas = values['frutas']
            paises = values['paises']
            objetos = values['objetos']

            for x in values:
                if values[x] == True:
                    escolha = x

            print(escolha)
            print(f'Frutas: {frutas}')
            print(f'paises: {paises}')
            print(f'objetos: {objetos}')


tela = JanelaJogo()
tela.Iniciar()
