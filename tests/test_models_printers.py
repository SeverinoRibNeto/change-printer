import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model_printers import *
import win32print
import pytest

def test_mudando_a_impressora_padrao_para_fax():
    #Give -Definir impressora atual
    current_printer = win32print.GetDefaultPrinter()
    new_default_printer = 'Fax'
    #When
    model_printer = Printer()
    model_printer.definir_impressora_padrao(new_default_printer)

    #Then
    assert win32print.GetDefaultPrinter() == new_default_printer
    model_printer.definir_impressora_padrao(current_printer)

def test_verifica_janela_ativa_e_igual_a_Code():
    #Given
    processo = "Code.exe" #Nome da janela ativa e processo esperado
    
    #When
    model_printer = Printer()
    

    #Then
    assert model_printer.janela_esta_ativa(processo) == True
    assert model_printer.janela_esta_ativa("winword.exe") == False

def test_pega_nome_do_processo_do_caminho_e_mostra_se_e_igual_a_Code():
    #Given
    processo = "Code.exe" #Nome da janela ativa e processo esperado
    caminho= "C:\\Users\\SeverinoRibeiroNeto\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    
    #When
    model_printer = Printer()
    
    #then
    assert model_printer.pegar_nome_processo(caminho) == processo.upper()

def test_pega_nome_do_processo_do_caminho_e_mostra_se_igual_a_Uptade_exe():
    #Given
    processo ="Update.exe"
    caminho="C:\\Users\\SeverinoRibeiroNeto\\AppData\\Local\\Discord\\Update.exe"

    #When
    model_printer = Printer()

    #then
    assert model_printer.pegar_nome_processo(caminho) == processo.upper()