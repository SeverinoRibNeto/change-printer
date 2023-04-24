from tkinter import Frame, Label, Button, Entry, ttk
import tkinter as tk


class Janela:

    def __init__(self, master:tk) -> None:
        self.janela_principal = master
        return

    def setup(self) -> None:
        self.create_widget()
        self.setup_layout()


    def create_widget(self)-> None:
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
        self.printersCbox = ttk.Combobox(self.dataFrame) #TODO: Colocar valores dentro da combobox
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
        """DataFrame"""
        self.dataFrame.grid(row=0, column=0)
        self.titleLb.grid(row=0, column=0, columnspan=3)
        self.printersCbox.grid(row=2, column=0, columnspan=3)
        self.archiveLb.grid(row=3, column=0, columnspan=3)
        self.pathEntry.grid(row=4, column=0, columnspan=2)
        self.openFileBtn.grid(row=4, column=2, columnspan=2)
        
        return


    def openFile(self):
        #TODO: implement this method
        pass


    def saveConfig(self):
        #TODO: implement this method
        pass


    def loadConfig(self):
        #TODO: implement this method
        pass


    def start(self):
        #TODO: implement this method
        pass

if __name__ == '__main__':
    root = tk.Tk()
    janela = Janela(root)
    root.mainloop()
