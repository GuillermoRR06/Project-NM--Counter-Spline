
DARK_THEME = """
QMainWindow, QWidget {
    background-color: #0B1120;
    color: #EAF2FF;
    font-family: "Segoe UI";
    font-size: 12px;
}

QFrame {
    background-color: #151F32;
    border: 1px solid #293B55;
    border-radius: 8px;
}

QLabel {
    color: #EAF2FF;
    border: none;
    background: transparent;
}

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

QListWidget {
    background-color: #0B1120;
    color: #EAF2FF;
    border: 1px solid #293B55;
    border-radius: 5px;
    padding: 5px;
}

QListWidget::item {
    padding: 7px;
    border-bottom: 1px solid #293B55;
}

QListWidget::item:selected {
    background-color: #16435A;
    color: #00D9FF;
}

QScrollBar:vertical {
    background: #0B1120;
    width: 8px;
}

QScrollBar::handle:vertical {
    background: #293B55;
    border-radius: 4px;
}

QFrame#gamePanel {
    background-color: #151F32;
    border: 1px solid #293B55;
    border-radius: 8px;
}

QLabel#panelTitle {
    color: #00D9FF;
    font-size: 13px;
    font-weight: bold;
    padding-bottom: 8px;
    border-bottom: 1px solid #293B55;
}
"""