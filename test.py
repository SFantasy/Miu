#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *


def main():
  
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(800, 600)
    w.move(300, 100)
    w.setWindowTitle('Miu')
    w.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
