#Simulador de um dado

import random
import PySimpleGUI as sg

class SimuladorDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = "Gostaria de jogar o dado?"

        #Parte gráfica
        self.layout = [
            [sg.Text("Gostaria de jogar o dado?")],
            [sg.Button("Sim")], [sg.Button("Não")]
        ]

        
    def Iniciar(self):
        self.janela = sg.Window("Simulador de Dado",self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == "Sim" or self.eventos == "n":
                self.GerarValorDoDado()
            elif self.eventos == "Não" or self.eventos == "n":
                print("Obrigado por acessar nosso dado.")
            else:
                print("Por favor responder com SIM ou NÃO.")
        except:
            print("Ocorreu um erro ao receber a sua resposta.")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_min,self.valor_max))



teste = SimuladorDado()
teste.Iniciar()
