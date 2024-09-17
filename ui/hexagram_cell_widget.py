from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from ui.hexagram_widget import HexagramWidget

class HexagramCellWidget(QWidget):
    clicked = pyqtSignal(object)

    def __init__(self, hexagram):
        super().__init__()
        self.hexagram = hexagram
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        self.hexagram_widget = HexagramWidget(self.hexagram)
        self.hexagram_widget.setFixedSize(60, 60)
        layout.addWidget(self.hexagram_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        label = QLabel(f"{self.hexagram.number}. {self.hexagram.name}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 12px;")
        layout.addWidget(label)

    def mousePressEvent(self, event):
        self.clicked.emit(self.hexagram)
        super().mousePressEvent(event)