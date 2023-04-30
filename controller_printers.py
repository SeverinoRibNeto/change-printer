from pubsub import pub
import os
import wx
import wx.xrc
from model_printers import Printer
from view_printers import GUI
from typing import List


class PrinterController:
    def __init__(self) -> None:
        self.running = False  # Abre o programa com a condição falsa

        printer = Printer()  # declaração da model printer
        self.app = wx.App()  # criação da interface gráfica
        self.frame = GUI(None)  # chamada da interface gráfica

        # preenche a lista de impressoras do sistema
        self.frame.m_choice2.SetItems(printer.lista_impressoras_instaladas())
        if (not os.path.exists('config.txt')):
            # Cria arquivo vazio com a configuração da impressora
            self.criar_arquivo_config('', '')

        # cria a comunicação com a view por meio de mensagens pubsub
        pub.subscribe(self.saveConfig, "Save_Config_Pressed")
        pub.subscribe(self.loadConfig, "Load_Config_Pressed")
        pub.subscribe(self.start, "Start_Pressed")
        pub.subscribe(self.stop, "Stop_Pressed")

    def saveConfig(self, caminho, impressora) -> bool:
        # salva caminho e impressora no arquivo config.txt
        self.criar_arquivo_config(caminho, impressora)
        # Desativa campos depois de salvar as configurações
        self.frame.m_choice2.Disable()
        self.frame.m_filePicker1.Disable()
        return True

    def loadConfig(self) -> None:
        """ Carrega uma lista, posição [0] - Path,
                               posição [1] - impressora padrão"""
        config = self.retorna_caminho_impressora_config()
        self.frame.m_choice2.SetStringSelection(config[1])
        self.frame.m_filePicker1.SetPath(config[0])

        # Desativa os campos depois de carregar as configurações
        self.frame.m_choice2.Disable()
        self.frame.m_filePicker1.Disable()

    def start(self, caminho: str, impressora: str) -> bool:
        # TODO: Implementar o looping de checagem de programa na model
        print("Start_Pressed - Controller")
        # Altera a label para mostrar o programa em funcionamento
        self.frame.m_staticText31.SetLabelText(
            text="Programa em funcionamento")
        self.running = True  # Variavel para rodar o loop do programa
        print(impressora, caminho)
        return True

    def stop(self):
        self.running = False
        self.frame.m_staticText31.SetLabelText(text="Programa Parado")
        print("Stop_Pressed - Controller")

    def criar_arquivo_config(self, caminho: str, impressora: str) -> bool:
        # Salva as configurações em um arquivo txt de nome config.txt
        try:
            with open('config.txt', "w") as f:
                f.write(f'caminho={caminho}')
                f.write('\n')
                f.write(f'impressora={impressora}')
                return True
        except Exception as e:
            print(e)
            return False

    def retorna_caminho_impressora_config(self) -> List[str]:
        # Pega o arquivo config.txt para ler as configurações
        try:
            with open('config.txt', "r") as f:
                config_caminho = f.readline()
                config_impressora = f.readline()

        except Exception as e:
            print(e)
        # Retorna uma lista com caminho na posição [0], impressora [1]
        return [config_caminho.split("=")[1].replace('\n', ''),
                config_impressora.split("=")[1]]


if __name__ == "__main__":
    printer = PrinterController()
    printer.frame.Show()
    printer.app.MainLoop()
