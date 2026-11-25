from PySide6.QtWidgets import QMainWindow
from interface.game_screen import GameScreen

# Ventana Principal
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter-Splines")
        self.resize(1200, 750)
        self.game_screen = GameScreen()
        self.setCentralWidget(self.game_screen)
        self.setMinimumSize(1000, 650)