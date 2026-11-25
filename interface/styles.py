DARK_THEME = """
/* =================================
   ESTILO GENERAL
================================= */

QMainWindow, QWidget {
    background-color: #0B1120;
    color: #EAF2FF;
    font-family: "Segoe UI";
    font-size: 12px;
}

/* =================================
   PANELES
================================= */

QFrame {
    background-color: #151F32;
    border: 1px solid #293B55;
    border-radius: 8px;
}

QFrame#gamePanel {
    background-color: #151F32;
    border: 1px solid #293B55;
    border-radius: 8px;
}

/* =================================
   ETIQUETAS
================================= */

QLabel {
    color: #EAF2FF;
    border: none;
    background: transparent;
}

QLabel#panelTitle {
    color: #00D9FF;
    font-size: 13px;
    font-weight: bold;
    padding-bottom: 8px;
    border-bottom: 1px solid #293B55;
}

/* Elementos informativos de la pantalla principal */

QLabel#turnLabel {
    color: #00D9FF;
    font-size: 14px;
    font-weight: bold;
}

QLabel#scoreLabel {
    color: #00E6A0;
    font-size: 14px;
    font-weight: bold;
}

QLabel#playersLabel {
    color: #00E6A0;
    font-size: 14px;
    font-weight: bold;
}

QLabel#dataLabel {
    color: #EAF2FF;
    font-size: 13px;
}

/* =================================
   BOTONES
================================= */

QPushButton {
    background-color: #102B40;
    color: #00D9FF;
    border: 1px solid #00D9FF;
    border-radius: 6px;
    padding: 10px 16px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #16435A;
    border: 1px solid #00E6A0;
    color: #00E6A0;
}

QPushButton:pressed {
    background-color: #00D9FF;
    color: #0B1120;
}

QPushButton:disabled {
    background-color: #182334;
    color: #52647D;
    border: 1px solid #293B55;
}

/* =================================
   LISTA DEL HISTORIAL
================================= */

QListWidget {
    background-color: #0B1120;
    color: #EAF2FF;
    border: 1px solid #293B55;
    border-radius: 5px;
    padding: 5px;
    outline: none;
}

QListWidget::item {
    padding: 7px;
    border-bottom: 1px solid #293B55;
}

QListWidget::item:hover {
    background-color: #102B40;
}

QListWidget::item:selected {
    background-color: #16435A;
    color: #00D9FF;
}

/* =================================
   BARRAS DE DESPLAZAMIENTO
================================= */

QScrollBar:vertical {
    background: #0B1120;
    width: 8px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: #293B55;
    border-radius: 4px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background: #00D9FF;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background: #0B1120;
    height: 8px;
    margin: 0;
}

QScrollBar::handle:horizontal {
    background: #293B55;
    border-radius: 4px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background: #00D9FF;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0;
}

/* =================================
   MENSAJES EMERGENTES
================================= */

QMessageBox {
    background-color: #151F32;
}

QMessageBox QLabel {
    color: #EAF2FF;
}

QToolTip {
    background-color: #151F32;
    color: #00D9FF;
    border: 1px solid #00D9FF;
    padding: 5px;
}
"""