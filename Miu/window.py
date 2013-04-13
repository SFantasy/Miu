#Filename: window.py

from Miu import *
from Miu.editor import MiuEditor

class MiuWindow(QMainWindow):
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.initConfig()
		self.resize(800, 600)
		