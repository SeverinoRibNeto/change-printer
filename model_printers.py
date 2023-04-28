import win32print
import win32gui
import win32process
import win32con
import win32api
import psutil
import os
from typing import List


class Printer:

    def __init__(self) -> None:
        return

    def lista_impressoras_instaladas(self) -> List[str]:
        # procura impressoras do sistema e retorna a lista
        return [impressora[2] for impressora in win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL,
            None,
            1)]

    def definir_impressora_padrao(self, nome_impressora_padrao: str) -> bool:
        # testa se impressora existe
        # Se o nome da impressora não tiver nas impressoras listadas,
        # lança erro
        if nome_impressora_padrao not in self.lista_impressoras_instaladas():
            raise ValueError("Impressora não instalada no sistema")
        # define a nova impressora padrão
        win32print.SetDefaultPrinter(nome_impressora_padrao)
        return True
    
    def janela_esta_ativa(self, nome_processo:str)->bool:
        #verifica a janela ativa
        janela_ativa = win32gui.GetForegroundWindow()
        #obter id do processo a partir do identificador da janela
        pid = win32process.GetWindowThreadProcessId(janela_ativa)[1]

        #obtem o handler do processo a partir do identificador
        handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 
                                          False, 
                                          pid)

        #obter nome do executavel do processo a partir do handle
        exe_file = win32process.GetModuleFileNameEx(handle, 0)

        print(exe_file)
        process_name = psutil.Process(pid).name()
        print("Nome do processo da janela ativa:", process_name)
        if process_name.upper() == nome_processo.upper():
            return True
        
        return False
    
    def pegar_nome_processo(self, caminho_processo:str) -> str:
        return os.path.basename(caminho_processo).upper() #Retorna o nome do processo pelo caminho


if __name__ == "__main__":
    impressora = Printer()
    print(impressora.janela_esta_ativa('Code.exe'))