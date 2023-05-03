import win32api
import win32con
import win32gui
import win32print
import win32process
import contextlib
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

    def janela_esta_ativa(self, nome_processo: str) -> bool:
        try:
            # Verifica a janela ativa
            janela_ativa = win32gui.GetForegroundWindow()

            # Obter id do processo a partir do identificador da janela
            pid = win32process.GetWindowThreadProcessId(janela_ativa)[1]

            # Obtem o handler do processo a partir do identificador
            with contextlib.closing(win32api.OpenProcess(
                win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ,
                False,
                pid
            )) as handle:

                # Obter nome do executavel do processo a partir do handle
                exe_file = win32process.GetModuleFileNameEx(handle, 0)

            process_name = psutil.Process(pid).name()

            return process_name.upper() == nome_processo.upper()

        except Exception:
            # Tratamento de exceções
            return False

    def pegar_nome_processo(self, caminho_processo: str) -> str:
        # Retorna o nome do processo pelo caminho
        return os.path.basename(caminho_processo).upper()


if __name__ == "__main__":
    impressora = Printer()
    print(impressora.janela_esta_ativa('Code.exe'))
