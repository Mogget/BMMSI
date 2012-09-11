# -*- coding: utf-8 -*-
"""
Główny plik. Uruchamiający program.


"""

import sys

# Odkomentować przed wysłaniem do repozytorium
#import sip
#sip.setapi('QString', 2)

from PyQt4 import QtGui

from bmmsi_window import BmmsiWindow

if __name__ == '__main__':
    """
    Uruchomienie aplikacji i przekazanie działania do Qt
    """
    
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
    app = QtGui.QApplication(sys.argv)
    SSN_app = BmmsiWindow()
    SSN_app.show()
    sys.exit(app.exec_())
    