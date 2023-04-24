from tkinter import Frame, Label, Button, Entry
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
        self.archiveLb = Label(self.dataFrame, text="Selecione o programa")
        """
            Entrys
        """
        self.pathEntry = Entry(self.dataFrame)
        """
            Combobox
        """

        """
            Buttons
        """
        self.openFileBtn = Button(self.dataFrame, 
                                  text="...",
                                  command=self.openFile)
        self.saveBtn = Button(self.dataFrame,
                              text="Salvar Configuração",
                              command=self.saveConfig)


    def setup_layout(self) -> None:
        self.container = tk.Frame(self.janela_principal)
        self.container.pack(side="top", fill="both", expand=True)
        self.dataFrame.pack(side="top", fill="both", expand=True)
        return


if __name__ == '__main__':
    root = tk.Tk()
    janela = Janela(root)
    root.mainloop()
