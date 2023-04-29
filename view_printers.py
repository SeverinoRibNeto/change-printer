# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.adv import TaskBarIcon as TaskBarIcon
from pubsub import pub
import pystray


###########################################################################
# Class TaskBar
###########################################################################
class TaskBar(TaskBarIcon):
    def __init__(self, frame):
        TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon('change-printer.png', wx.BITMAP_TYPE_PNG), 'Task bar icon')

        #----------------------------------------------------------------
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarDeactivate, id=2)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=3)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, "Mostrar")
        menu.Append(2, "Esconder")
        menu.Append(3, "Fechar")
        return menu
    
    def OnTaskBarActivate(self, event):
        if (not self.frame.IsShown()):
            self.frame.Show()

    def OnTaskBarDeactivate(self, event):
        if (self.frame.IsShown()):
            self.frame.Hide()
    
    def OnTaskBarClose(self, event):
        self.frame.Close()
        
        


###########################################################################
# Class GUI
###########################################################################


class GUI (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GIP",
                          pos=wx.DefaultPosition, size=wx.Size(722, 335),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetIcon(wx.Icon('change-printer.ico', wx.BITMAP_TYPE_ICO))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        #----------------------------------------------------------------
        self.tskic = TaskBar(self)
        #----------------------------------------------------------------
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #----------------------------------------------------------------
        self.message_box_program = wx.MessageDialog(self, 
                                       "Coloque o programa a ser usado pela impressora.", 
                                       caption="Error",
                                       style=wx.OK_DEFAULT|wx.CENTER)
        self.message_box_printer= wx.MessageDialog(self, 
                                       "Selecione a impressora padrão para o programa.", 
                                       caption="Error",
                                       style=wx.OK_DEFAULT|wx.CENTER)

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

        gSizer1 = wx.GridSizer( 1, 4, 0, 0 )

        self.saveConfBtn = wx.Button( self, wx.ID_ANY, u"Salvar Configurações", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.saveConfBtn.SetMinSize( wx.Size( 150,40 ) )

        gSizer1.Add( self.saveConfBtn, 0, wx.ALL, 5 )

        self.loadConfBtn = wx.Button( self, wx.ID_ANY, u"Carregar Configuração", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.loadConfBtn.SetMinSize( wx.Size( 150,40 ) )

        gSizer1.Add( self.loadConfBtn, 0, wx.ALL, 5 )

        self.startBtn = wx.Button( self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.startBtn.SetMinSize( wx.Size( 150,40 ) )

        gSizer1.Add( self.startBtn, 0, wx.ALL, 5 )

        self.pararBtn = wx.Button( self, wx.ID_ANY, u"Parar", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.pararBtn.SetMinSize( wx.Size( 150,40 ) )

        gSizer1.Add( self.pararBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )


        bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Programa Parado", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer2.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.saveConfBtn.Bind(wx.EVT_BUTTON, self.saveConfig)
        self.loadConfBtn.Bind(wx.EVT_BUTTON, self.loadConfig)
        self.startBtn.Bind(wx.EVT_BUTTON, self.start)
        self.pararBtn.Bind( wx.EVT_BUTTON, self.stop )

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
                        caminho_processo=self.m_filePicker1.GetPath(), 
                        impressora_selecionada=self.m_choice2.GetStringSelection())
        event.Skip()

    def loadConfig(self, event):
        pub.sendMessage("Load_Config_Pressed")
        event.Skip()

    def start(self, event) -> None:
        if not (self.m_choice2.GetStringSelection()):
            self.message_box_printer.ShowModal()
            return
        
        if not (self.m_filePicker1.GetPath()):
            self.message_box_program.ShowModal()
            return
        
        pub.sendMessage("Start_Pressed", 
                        caminho_processo=self.m_filePicker1.GetPath(), 
                        impressora_selecionada=self.m_choice2.GetStringSelection())
        event.Skip()
    
    
    def stop( self, event ):
        pub.sendMessage("Stop_Pressed")
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = GUI(None)
    frame.Show()
    app.MainLoop()
