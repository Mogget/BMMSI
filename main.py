# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:13:31 2012

@author: bzyx
"""
import sys

import sip
sip.setapi('QString', 2)

from PyQt4 import QtGui

from silnik import demo
from bmmsi_window import BmmsiWindow

if __name__ == '__main__':
    #demo()
    app = QtGui.QApplication(sys.argv)
    SSN_app = BmmsiWindow()
    SSN_app.show()
    sys.exit(app.exec_())
    