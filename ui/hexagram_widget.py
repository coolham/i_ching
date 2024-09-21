from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QFont, QColor
from ui.hexagram_diagram import HexagramDiagram

class HexagramWidget(QWidget):
    hexagramClicked = pyqtSignal(object)

    def __init__(self, hexagram=None, yang_color=QColor(255, 0, 0), parent=None):
        super().__init__(parent)
        self.hexagram = hexagram
        layout = QVBoxLayout(self)
        layout.setSpacing(15)  # 增加间距

        self.diagram = HexagramDiagram(hexagram, yang_color=yang_color)
        layout.addWidget(self.diagram, alignment=Qt.AlignmentFlag.AlignCenter)

        self.name_label = QLabel()
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setStyleSheet("font-size: 24px; color: #333;")
        self.name_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(self.name_label)

        self.mousePressEvent = self.widget_clicked

        if hexagram:
            self.update_hexagram(hexagram)

    def update_hexagram(self, hexagram):
        self.hexagram = hexagram
        self.diagram.update_hexagram(hexagram)
        self.name_label.setText(hexagram.name)
        self.setToolTip(f"{hexagram.name} - {hexagram.mnemonic}")

    def widget_clicked(self, event):
        if self.hexagram:
            self.hexagramClicked.emit(self.hexagram)

    def sizeHint(self):
        return QSize(200, 300)  # 调整建议尺寸