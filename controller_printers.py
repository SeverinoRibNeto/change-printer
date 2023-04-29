from pubsub import pub
import wx, wx.xrc
from model_printers import Printer
from view_printers import GUI
from typing import List
class PrinterController:
    def __init__(self) -> None:
        printer = Printer()
        self.app = wx.App()
        self.frame = GUI(None)
        impressoras_instaladas = printer.lista_impressoras_instaladas()
        self.frame.m_choice2.SetItems(impressoras_instaladas)
        
        pub.subscribe(self.saveConfig, "Save_Config_Pressed")
        pub.subscribe(self.loadConfig, "Load_Config_Pressed")
        pub.subscribe(self.start, "Start_Pressed")



    def saveConfig(self, caminho_processo, impressora_selecionada) -> bool:
        #Salva as configurações em um arquivo txt de nome config.txt
        try:
            with open('config.txt', "w") as f:
                f.write(f'caminho={caminho_processo}')
                f.write('\n')
                f.write(f'impressora={impressora_selecionada}')
        except Exception as e:
            print(e)
        print("Save_Config_Pressed - Controller")

    def loadConfig(self) -> None:
        print(self.retorna_caminho_impressora_config())
        print("Load_Config_Pressed - Controller")

    def start(self, caminho_processo, impressora_selecionada) -> bool:
        print("Start_Pressed - Controller")
        print(impressora_selecionada, caminho_processo)
        return True

    def retorna_caminho_impressora_config(self) -> List[str]:
        try:
            with open('config.txt', "r") as f:
                config_caminho = f.readline()
                config_impressora = f.readline()

        except Exception as e:
            print(e)

        print(config_caminho)
        return [config_caminho.split("=")[1].replace('\n',''), config_impressora.split("=")[1]]


if __name__ == "__main__":
    printer = PrinterController()
    printer.frame.Show()
    printer.app.MainLoop()