import PySimpleGUI as sg
import listasPalavras as lp
import forcaDesenhos

class JanelaJogo:

    def __init__(self):
        # Layout
        sg.theme('DarkBlue2')
        layout = [  
                    [sg.Text('Bem vindo ao Jogo de Forca!!!')],
                    [sg.Text('Escolha uma categoria uma das categorias para iniciar:')],
                    [sg.Radio('Frutas','opcao', default=True, key='frutas'), sg.Radio('Países','opcao',key='paises'),
                     sg.Radio('Objetos','opcao', key='objetos')],
                    [sg.Text('Digite uma letra e pressiione OK'), sg.Input(size=(3,0), key='letra'), sg.Button('Ok')],
                    [sg.Output(size=(50, 30), key='output')],
                    [sg.Button('Sair')]
                ]

        # Janela

        self.janela = sg.Window('Jogo da Forca', layout)

               
    def Iniciar(self):
        palavra_secreta = lp.define_palavra_chave()
        lista_palavra = ["_" for letra in palavra_secreta]
        palavra_tamanho = len(lista_palavra)
        tentativas = 6
        rodada = 1
        erros = 0
        enforcou = False
        acertou = False
        while True:
            event, values = self.janela.read()
            
            self.janela.find_element('output').update('')
            frutas = values['frutas']
            paises = values['paises']
            objetos = values['objetos']
            letra = values['letra']


            for x in values:
                if values[x] == True:
                    escolha = x

            print(f'palavra_chave: {palavra_secreta}')
            print(f'Categoria: {escolha.upper()}\
                        Número de letras {palavra_tamanho}\n\n')
            
            if event == sg.WIN_CLOSED or event == 'Sair':
                break

            if (not acertou and not enforcou):
                print(f'Tentativa {rodada} de {tentativas}')
                rodada = rodada + 1

                chute = letra
                chute = chute.strip().upper()

                posicao = 0

                if(chute in palavra_secreta):
                    for letra in palavra_secreta:
                        if (chute.upper() == letra.upper()):
                            lista_palavra[posicao] = letra
                        posicao = posicao + 1

                else:
                    erros += 1
                    
                print(f' {forcaDesenhos.desenha_forca(erros)} ')
                print(f' {lista_palavra}')
                enforcou = erros == 7
                acertou = "_" not in lista_palavra
                values['letra'] = ''

            if (acertou):
                forcaDesenhos.imprime_mensagem_vencedor()
            elif (enforcou):
                forcaDesenhos.imprime_mensagem_perdedor(palavra_secreta)

tela = JanelaJogo()
tela.Iniciar()
