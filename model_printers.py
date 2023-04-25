import win32print
from typing import List


def lista_impressoras_instaladas() -> List[str]:
    # procura impressoras do sistema e retorna a lista
    return [impressora[2] for impressora in win32print.EnumPrinters(
        win32print.PRINTER_ENUM_LOCAL,
        None,
        1)]


def definir_impressora_padrao(nome_impressora_padrao: str) -> bool:
    # testa se impressora existe
    # Se o nome da impressora não tiver nas impressoras listadas, lança erro
    if (not (nome_impressora_padrao in lista_impressoras_instaladas())):
        raise ValueError("Impressora não instalada no sistema")
    # define a nova impressora padrão
    win32print.SetDefaultPrinter(nome_impressora_padrao)
    return True
