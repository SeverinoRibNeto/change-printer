# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"GIP",
                          pos=wx.DefaultPosition, size=wx.Size(722, 335),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

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

        m_choice2Choices = [u"Selecione a impressora", wx.EmptyString]
        self.m_choice2 = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition,
            wx.Size(300, -1), m_choice2Choices, 0)
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

        gSizer1 = wx.GridSizer(1, 3, 0, 0)

        self.saveConfBtn = wx.Button(
            self, wx.ID_ANY, u"Salvar Configurações",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.saveConfBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.saveConfBtn, 0, wx.ALL, 5)

        self.loadConfBtn = wx.Button(
            self, wx.ID_ANY, u"Carregar Configuração",
            wx.DefaultPosition, wx.DefaultSize, 0)
        self.loadConfBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.loadConfBtn, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.startBtn = wx.Button(
            self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.startBtn.SetMinSize(wx.Size(150, 40))

        gSizer1.Add(self.startBtn, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.saveConfBtn.Bind(wx.EVT_BUTTON, self.saveConfig)
        self.loadConfBtn.Bind(wx.EVT_BUTTON, self.loadConfig)
        self.startBtn.Bind(wx.EVT_BUTTON, self.start)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def saveConfig(self, event):
        event.Skip()

    def loadConfig(self, event):
        event.Skip()

    def start(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
