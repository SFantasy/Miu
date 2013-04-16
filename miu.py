#Filename: miu.py

import sys

from Miu import *
from Miu.window import MiuWindow

def main():
	app = QApplication(sys.argv)
	app.setOrganizationName("Miu Project")
	app.setApplicationName("Miu")	

	window = MiuWindow()
	window.show()

	sys.exit(app.exec_())


if __name__ == '__main__':
	main()