from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QListWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QMessageBox)
from PySide6.QtCore import Qt
from interface.graph_widget import GraphWidget

# Pantalla Principal
class GameScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.data_visible = False
        self.current_player = "Jugador 1"
        self.create_interface()

    def create_interface(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Parte Superior
        top_layout = QHBoxLayout()

        self.reveal_button = QPushButton("REVELAR DATOS")
        self.reveal_button.clicked.connect(self.reveal_data)

        self.turn_label = QLabel("TURNO: JUGADOR 1")
        self.score_label = QLabel("P1: 0   |   P2: 0")

        top_layout.addWidget(self.reveal_button)
        top_layout.addStretch()
        top_layout.addWidget(self.turn_label)
        top_layout.addStretch()
        top_layout.addWidget(self.score_label)

        main_layout.addLayout(top_layout)

        # Parte Central
        center_layout = QGridLayout()
        center_layout.setSpacing(12)

        # Panel de datos
        self.data_panel = self.create_panel("DATOS")

        self.data_label = QLabel(
            "Datos ocultos.\nPresiona Revelar datos."
        )

        self.data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_panel.layout().addWidget(self.data_label)

        # Gráfico
        graph_panel = self.create_panel("MAPEO DE FUNCIONES")

        self.graph = GraphWidget()
        graph_panel.layout().addWidget(self.graph)

        # Botón atacar
        attack_panel = self.create_panel("ATAQUE")

        self.attack_button = QPushButton("ATACAR")
        self.attack_button.clicked.connect(self.attack)

        attack_panel.layout().addWidget(self.attack_button)

        center_layout.addWidget(self.data_panel, 0, 0)
        center_layout.addWidget(graph_panel, 0, 1)
        center_layout.addWidget(attack_panel, 0, 2)

        center_layout.setColumnStretch(0, 1)
        center_layout.setColumnStretch(1, 3)
        center_layout.setColumnStretch(2, 1)

        main_layout.addLayout(center_layout, stretch=3)

        # Parte inferior
        bottom_layout = QHBoxLayout()

        # Historial
        history_panel = self.create_panel(
            "HISTORIAL DE FUNCIONES"
        )

        self.history_list = QListWidget()

        self.history_list.addItems([
            "f(x) = x²",
            "f(x) = 2x + 1",
            "f(x) = x³ - 2x"
        ])

        history_panel.layout().addWidget(self.history_list)

        # Jugadores activos
        players_panel = self.create_panel(
            "JUGADORES ACTIVOS"
        )

        self.players_label = QLabel("2 jugadores vivos")
        self.players_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        players_panel.layout().addWidget(self.players_label)

        # Interpolar
        interpolation_panel = self.create_panel(
            "INTERPOLACION"
        )

        self.interpolate_button = QPushButton("INTERPOLAR")
        self.interpolate_button.clicked.connect(
            self.interpolate
        )

        interpolation_panel.layout().addWidget(
            self.interpolate_button
        )

        bottom_layout.addWidget(history_panel, stretch=2)
        bottom_layout.addWidget(players_panel, stretch=1)
        bottom_layout.addWidget(interpolation_panel, stretch=1)

        main_layout.addLayout(bottom_layout, stretch=1)

    # Funciones Auxiliares
    def create_panel(self, title):
        panel = QFrame()
        panel.setObjectName("gamePanel")

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName("panelTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)

        return panel

    def reveal_data(self):
        self.data_visible = not self.data_visible

        if self.data_visible:
            self.data_label.setText(
                "Jugador 1\n\n"
                "Coordenadas:\n"
                "X: 3.5\n"
                "Y: 2.0"
            )

            self.reveal_button.setText("OCULTAR DATOS")

        else:
            self.data_label.setText(
                "Datos ocultos.\nPresiona Revelar datos."
            )

            self.reveal_button.setText("REVELAR DATOS")

    def attack(self):
        QMessageBox.information(
            self,
            "Ataque",
            "Aqui se abrira la pantalla de ataque."
        )

    def interpolate(self):
        QMessageBox.information(
            self,
            "Interpolación",
            "Aquí se abrirá la pantalla de interpolación."
        )