# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os
import wx
import wx.xrc
from wx.adv import TaskBarIcon as TaskBarIcon
from pubsub import pub


###########################################################################
# Class TaskBar
###########################################################################
class TaskBar(TaskBarIcon):
    def __init__(self, frame:wx.Frame, path_icon: os.path) -> None:
        TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(path_icon,
                     wx.BITMAP_TYPE_PNG), 'Task bar icon')
        # Variable to indicate if program is running or not
        self.running = False

        # ----------------------------------------------------------------
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivateDeactivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=2)
        self.Bind(wx.EVT_MENU, self.OnTaskBarStartStop, id=3)

# Create a popup menu and items
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, "Mostrar/Esconder")
        menu.Append(2, "Fechar")
        menu.Append(3, "Iniciar/Parar")

        return menu

# Create function to show or hide a windows if frame.
    def OnTaskBarActivateDeactivate(self, event):
        if (not self.frame.IsShown()):
            self.frame.Show()
        elif (self.frame.IsShown()):
            self.frame.Hide()

# Function close the program
    def OnTaskBarClose(self, event):
        self.frame.Close()

# Function start script or stop depending on value of running
    def OnTaskBarStartStop(self, event):
        if not (self.running):
            self.running = True
            pub.sendMessage("Start_Pressed")
        else:
            self.running = False
            pub.sendMessage("Stop_Pressed")

###########################################################################
# Class GUI
###########################################################################


class GUI (wx.Frame):

    def __init__(self, parent, path_icon: os.path) -> None:
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GIP",
                          pos=wx.DefaultPosition, size=wx.Size(722, 335),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetIcon(wx.Icon(path_icon, wx.BITMAP_TYPE_PNG))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        # ----------------------------------------------------------------
        self.tskic = TaskBar(self, path_icon)
        # ----------------------------------------------------------------
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # ----------------------------------------------------------------
        program_message = "Coloque o programa a ser usado pela impressora."
        printer_message = "Selecione a impressora padrão para o programa."
        self.message_box_program = wx.MessageDialog(self,
                                                    program_message,
                                                    caption="Error",
                                                    style=wx.OK_DEFAULT)
        self.message_box_printer = wx.MessageDialog(self,
                                                    printer_message,
                                                    caption="Error",
                                                    style=wx.OK_DEFAULT)
        # ----------------------------------------------------------------
        self.running = False
        # ----------------------------------------------------------------
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"Selecione uma impressora:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetFont(wx.Font(
            14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL, False, "Arvo"))

        bSizer1.Add(self.m_staticText3, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_choice2Choices = [u"Selecione a impressora", wx.EmptyString]
        self.m_choice2 = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition,
            wx.Size(300, -1), self.m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        self.m_choice2.SetFont(wx.Font(
            14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL, False, "Arvo"))

        bSizer1.Add(self.m_choice2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText4 = wx.StaticText(
            self, wx.ID_ANY, u"Selecione o programa:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.SetFont(wx.Font(
            14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL, False, "Arvo"))

        bSizer1.Add(self.m_staticText4, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_filePicker1 = wx.FilePickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Escolha o programa", u"*.exe",
            wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        self.m_filePicker1.SetMinSize(wx.Size(300, -1))

        bSizer1.Add(self.m_filePicker1, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(1, 4, 0, 0)

        self.saveConfBtn = wx.Button(
            self, wx.ID_ANY,
            u"Salvar Configurações",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.saveConfBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.saveConfBtn, 0, wx.ALL, 5)

        self.loadConfBtn = wx.Button(
            self, wx.ID_ANY,
            u"Carregar Configuração",
            wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.loadConfBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.loadConfBtn, 0, wx.ALL, 5)

        self.start_stopBtn = wx.Button(self,
                                       wx.ID_ANY,
                                       u"Iniciar / Parar",
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       0)
        self.start_stopBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.start_stopBtn, 0, wx.ALL, 5)

        self.hideBtn = wx.Button(self,
                                 wx.ID_ANY,
                                 u"Esconder",
                                 wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        self.hideBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.hideBtn, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer1.Add(gSizer1, 0, wx.EXPAND, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText31 = wx.StaticText(
            self, wx.ID_ANY,
            u"Programa Parado",
            wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)

        bSizer2.Add(self.m_staticText31, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.saveConfBtn.Bind(wx.EVT_BUTTON, self.saveConfig)
        self.loadConfBtn.Bind(wx.EVT_BUTTON, self.loadConfig)
        self.start_stopBtn.Bind(wx.EVT_BUTTON, self.start_stop)
        self.hideBtn.Bind(wx.EVT_BUTTON, self.hide)

    def __del__(self):
        pass

    def OnClose(self, event):
        self.tskic.Destroy()
        self.Destroy()

    # Virtual event handlers, override them in your derived class
    def saveConfig(self, event):
        if not (self.m_choice2.GetStringSelection()):
            self.message_box_printer.ShowModal()
            return

        if not (self.m_filePicker1.GetPath()):
            self.message_box_program.ShowModal()
            return
        pub.sendMessage("Save_Config_Pressed",
                        caminho=self.m_filePicker1.GetPath(),
                        impressora=self.m_choice2.GetStringSelection())
        event.Skip()

    def loadConfig(self, event):
        pub.sendMessage("Load_Config_Pressed")
        event.Skip()

    def start_stop(self, event) -> None:
        if not (self.m_choice2.GetStringSelection()):
            self.message_box_printer.ShowModal()
            return

        elif not (self.m_filePicker1.GetPath()):
            self.message_box_program.ShowModal()
            return

        if not (self.running):
            self.running = True
            pub.sendMessage("Start_Pressed",
                            caminho=self.m_filePicker1.GetPath(),
                            impressora=self.m_choice2.GetStringSelection())
        elif (self.running):
            self.running = False
            pub.sendMessage("Stop_Pressed")
        event.Skip()

    def hide(self, event):
        if (self.IsShown()):
            self.Hide()
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = GUI(None, os.path.join(os.path.join(os.getcwd(), 'change-printer.png')))
    frame.Show()
    app.MainLoop()
