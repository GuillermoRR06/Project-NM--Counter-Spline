from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QListWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QMessageBox, QSizePolicy)
from PySide6.QtCore import Qt
from interface.graph_widget import GraphWidget

# Pantalla Principal
class GameScreen(QWidget):

    def __init__(self):
        super().__init__()

        # Estado de la partida
        self.data_visible = False
        self.current_player = 1

        # Puntuaciones
        self.scores = {1: 0, 2: 0}

        # Datos de los jugadores
        self.player_data = {
            1: {"x": 3.5, "y": 2.0},
            2: {"x": -2.0, "y": 4.0}
        }

        # Jugadores activos
        self.active_players = [1, 2]

        # Historial de funciones
        self.function_history = [
            "f(x) = x²",
            "f(x) = 2x + 1",
            "f(x) = x³ - 2x"
        ]

        self.create_interface()


    def create_interface(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(12)

        # Parte Superior
        top_layout = QHBoxLayout()

        self.reveal_button = QPushButton("REVELAR DATOS")
        self.reveal_button.clicked.connect(self.reveal_data)
        self.end_turn_button = QPushButton("FINALIZAR TURNO")
        self.end_turn_button.clicked.connect(self.end_turn)

        self.turn_label = QLabel("TURNO: JUGADOR 1")
        self.score_label = QLabel("P1: 0   |   P2: 0")
        self.turn_label.setObjectName("turnLabel")
        self.score_label.setObjectName("scoreLabel")

        top_layout.addWidget(self.reveal_button)
        top_layout.addWidget(self.end_turn_button)
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
        self.data_panel.setMinimumWidth(190)
        self.data_panel.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Expanding)

        self.data_label = QLabel("Datos ocultos.\nPresiona Revelar datos.")
        self.data_label.setObjectName("dataLabel")

        self.data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_panel.layout().addWidget(self.data_label)

        # Gráfico
        graph_panel = self.create_panel("MAPEO DE FUNCIONES")
        graph_panel.setMinimumHeight(340)

        self.graph = GraphWidget()
        self.graph.setMinimumHeight(280)
        self.graph.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        graph_panel.layout().addWidget(self.graph)

        # Botón atacar
        attack_panel = self.create_panel("ATAQUE")
        attack_panel.setMinimumWidth(190)

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
        bottom_layout.setSpacing(12)

        # Historial
        history_panel = self.create_panel("HISTORIAL DE FUNCIONES")
        history_panel.setMinimumWidth(300)
        history_panel.setMinimumHeight(160)

        self.history_list = QListWidget()
        self.history_list.addItems(self.function_history)

        history_panel.layout().addWidget(self.history_list)

        # Jugadores activos
        players_panel = self.create_panel("JUGADORES ACTIVOS")
        players_panel.setMinimumHeight(160)

        self.players_label = QLabel("2 jugadores vivos")
        self.players_label.setObjectName("playersLabel")
        self.players_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        players_panel.layout().addWidget(self.players_label)

        # Interpolar
        interpolation_panel = self.create_panel("INTERPOLACION")
        interpolation_panel.setMinimumHeight(160)

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
        
        self.update_score_display()
        self.update_turn_display()
        self.update_players_display()

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

    # Mostrar las puntuaciones actuales
    def update_score_display(self):
        self.score_label.setText(f"P1: {self.scores[1]}   |   P2: {self.scores[2]}")

    # Mostrar el jugador que tiene el turno
    def update_turn_display(self):
        self.turn_label.setText(f"TURNO: JUGADOR {self.current_player}")

    # Mostrar cuántos jugadores siguen activos
    def update_players_display(self):
        count = len(self.active_players)
        self.players_label.setText(f"{count} jugadores vivos")

    def reveal_data(self):
        self.data_visible = not self.data_visible
        if self.data_visible:
            # Obtener los datos del jugador actual
            data = self.player_data[self.current_player]
            self.data_label.setText(
                f"JUGADOR {self.current_player}\n\n"
                "Coordenadas:\n"
                f"X: {data['x']}\n"
                f"Y: {data['y']}")
            self.reveal_button.setText("OCULTAR DATOS")
        else:
            self.data_label.setText("Datos ocultos.\nPresiona Revelar datos.")
            self.reveal_button.setText("REVELAR DATOS")
    
    
    def end_turn(self):

        # Comprobar que existan jugadores activos
        if not self.active_players:
            return

        # Determinar el siguiente jugador activo
        if self.current_player in self.active_players:
            current_index = self.active_players.index(self.current_player)
            next_index = (current_index + 1) % len(self.active_players)
            self.current_player = self.active_players[next_index]
        else:
            self.current_player = self.active_players[0]

        # Ocultar los datos del turno anterior
        self.data_visible = False
        self.data_label.setText("Datos ocultos.\nPresiona Revelar datos.")
        self.reveal_button.setText("REVELAR DATOS")

        # Actualizar la información del turno
        self.update_turn_display()

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