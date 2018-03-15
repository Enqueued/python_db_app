import sqlite3
import sys
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMizin, ListCtrlAutoWidthMixin

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs)
        wx.Dialog.__init__(self, None, title="Records", size=(600,400))
        
        info_label = wx.StaticText(self, label='Please Enter INFO below')
        self.first_name wx.TextCtrl(self, -1, '')
        wx.StaticText(self, -1, 'First Name')

        
