# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frMain
###########################################################################

class frMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Konversi DXF ke CMZ", pos = wx.DefaultPosition, size = wx.Size( 352,235 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Apa yang kamu mau lakukan?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.btnConvert = wx.Button( self, wx.ID_ANY, u"Konversi DXF ke CMZ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnConvert, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnEdit = wx.Button( self, wx.ID_ANY, u"Edit file CMZ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnEdit, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnConvert.Bind( wx.EVT_BUTTON, self.btnConvertOnButtonClick )
		self.btnEdit.Bind( wx.EVT_BUTTON, self.btnEditOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btnConvertOnButtonClick( self, event ):
		event.Skip()

	def btnEditOnButtonClick( self, event ):
		event.Skip()


