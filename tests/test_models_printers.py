import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from printers import *
import win32print
import pytest

def test_mudando_a_impressora_padrao_para_fax():
    #Give -Definir impressora atual
    current_printer = win32print.GetDefaultPrinter()
    new_default_printer = 'Fax'
    #When
    definir_impressora_padrao(new_default_printer)

    #Then
    assert win32print.GetDefaultPrinter() == new_default_printer
    definir_impressora_padrao(current_printer)