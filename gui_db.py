import sqlite3
import sys
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Dialog.__init__(self, None, title="Records", size=(600,400))
        app = wx.App()
        window = wx.Frame(None, title = "", size=(something))

        '''
        below are the labels and buttons that will be displayed on the gui
        '''
        info_label = wx.StaticText(self, label='Please Enter INFO below')

        '''
        first name field
        '''
        self.first_name = wx.TextCtrl(self, -1, '')
        wx.StaticText(self, -1, 'First Name')

        '''
        last name field
        '''
        self.last_name = wx.TextCtrl(self, -1, '')
        wx.StaticText(self, -1, 'Last Name')

        '''
        Admission date
        '''
        self.admiss = wx.TextCtrl(self, -1, '')
        wx.StaticText(self, -1, 'Admission Date')

        '''
        Care term
        '''
        self.term = wx.TextCtrl(self, -1, '')
        wx.StaticText(self, -1, 'Term of Care')

