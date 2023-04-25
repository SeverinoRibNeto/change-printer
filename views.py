from tkinter import Frame, Label, Button, Entry, ttk, Tk
import tkinter as tk
import tkinter.font as tkFont


class GUI:

    def __init__(self, master: tk.Tk) -> None:
        self.janela_principal = master
        return

    def setup(self) -> None:
        self.create_widget()
        self.setup_layout()

    def create_widget(self) -> None:
        """
            Create a frame
        """
        self.dataFrame = Frame(self.janela_principal, borderwidth=1,
                               highlightbackground="black")
        """
            Create Labels
        """
        self.titleLb = Label(self.dataFrame, text="Selecione a impressora:")
        self.archiveLb = Label(self.dataFrame, text="Selecione o programa:")
        """
            Entrys
        """
        self.pathEntry = Entry(self.dataFrame)
        """
            Combobox
        """
        self.printersCbox = ttk.Combobox(
            self.dataFrame)  # TODO: Colocar valores dentro da combobox
        """
            Buttons
        """
        self.openFileBtn = Button(self.dataFrame,
                                  text="...",
                                  command=self.openFile)
        self.saveBtn = Button(self.dataFrame,
                              text="Salvar Configuração",
                              command=self.saveConfig)
        self.loadConfigBtn = Button(self.dataFrame,
                                    text="Carregar Configuração",
                                    command=self.loadConfig)
        self.startBtn = Button(self.dataFrame,
                               text="Iniciar",
                               command=self.start)

    def setup_layout(self) -> None:
        font_style = tkFont.Font(family="Arial", size=14, weight='normal')
        """DataFrame"""
        self.dataFrame.grid(row=0, column=0)
        self.titleLb.grid(row=0, column=2, columnspan=3)
        self.titleLb.configure(font=font_style)
        self.printersCbox.grid(row=2, column=2, columnspan=3)
        self.printersCbox.configure(font=font_style)
        self.archiveLb.grid(row=3, column=2, columnspan=3)
        self.archiveLb.configure(font=font_style)
        self.pathEntry.grid(row=4, column=3, columnspan=2)
        self.pathEntry.configure(font=font_style)
        self.openFileBtn.grid(row=4, column=6, columnspan=2)
        self.openFileBtn.configure(font=font_style)

        return

    def openFile(self):
        # TODO: implement this method
        pass

    def saveConfig(self):
        # TODO: implement this method
        pass

    def loadConfig(self):
        # TODO: implement this method
        pass

    def start(self):
        # TODO: implement this method
        pass


if __name__ == '__main__':
    mainwin = Tk()
    width = 450
    height = 450
    mainwin.geometry(f'{width}x{height}')
    mainwin.title('GIP')

    gui = GUI(mainwin)
    gui.setup()
    mainwin.mainloop()
