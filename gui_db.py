import sqlite3
import sys
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMizin, ListCtrlAutoWidthMixin

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs)
        wx.Dialog.__init__(self, None, title="Records", size=(600,400))
