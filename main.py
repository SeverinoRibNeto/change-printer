import win32print
import win32gui
import time
import pystray

impressoras = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1) #Obtem listas de impressoras no sistema


current_print = win32print.GetDefaultPrinter()
print(current_print)