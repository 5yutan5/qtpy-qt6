from ..qt_compat import QT_API

if QT_API == "PySide6":
    from PySide6.QtCore import *
elif QT_API == "PyQt6":
    from PyQt6.QtCore import *

    Slot = pyqtSlot
    Signal = pyqtSignal
    del pyqtSlot
    del pyqtSignal
elif QT_API == "PyQt5":
    from PyQt5.QtCore import *

    Slot = pyqtSlot
    Signal = pyqtSignal
    del pyqtSlot
    del pyqtSignal
elif QT_API == "PySide2":
    from PySide2.QtCore import *
