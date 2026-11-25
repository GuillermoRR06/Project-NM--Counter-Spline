'''
Ejecutar en consola: python main.py
'''
import sys
from PySide6.QtWidgets import QApplication
from interface.main_window import MainWindow
from interface.styles import DARK_THEME

# Ejecutar
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(DARK_THEME)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())