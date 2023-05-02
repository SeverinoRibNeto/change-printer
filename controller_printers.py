from pubsub import pub
import os
import wx
import wx.xrc
import asyncio
import time
import win32print
from threading import Event
import threading
from model_printers import Printer
from view_printers import GUI
from typing import List


class PrintThread(threading.Thread):
    def __init__(self, caminho_processo:str, impressora:str) -> None:
        threading.Thread.__init__(self)
        self.caminho = caminho_processo
        self.impressora = impressora
        self.default_printer = win32print.GetDefaultPrinter()
        self.to_stop = False
    
    def run(self) -> None:
        while True:
            time.sleep(0.5)
            self.check_active_window_update_printer()
            if self.to_stop:
                return None

    def check_active_window_update_printer(self)->None:
        printer = Printer()
        process_name = printer.pegar_nome_processo(self.caminho)
        if printer.janela_esta_ativa(process_name):
            printer.definir_impressora_padrao(self.impressora)
        elif not printer.janela_esta_ativa(process_name):
            printer.definir_impressora_padrao(self.default_printer)
        print("Checking active window")

class PrinterController:
    def __init__(self) -> None:
        self.running = False  # Abre o programa com a condição falsa
        self.task = None
        self.printer = Printer()  # declaração da model printer
        self.app = wx.App()  # criação da interface gráfica
        self.frame = GUI(None)  # chamada da interface gráfica

        # preenche a lista de impressoras do sistema
        self.frame.m_choice2.SetItems(self.printer.lista_impressoras_instaladas())
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

    def start(self, caminho: str, impressora: str) -> None:
        self.running = True
        self.pt = PrintThread(caminho_processo=caminho, impressora=impressora)
        default_printer = win32print.GetDefaultPrinter()
        processo = self.printer.pegar_nome_processo(caminho)
        self.pt.start()
        self.frame.m_staticText31.SetLabelText(
            text="Programa Inicializado")

    def stop(self):
        self.pt.to_stop = True
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
            

    def run(self):
        self.frame.Show()
        self.app.MainLoop()

if __name__ == "__main__":
    controller = PrinterController()
    controller.run()
