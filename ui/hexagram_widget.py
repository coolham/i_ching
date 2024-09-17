from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QFont
from ui.hexagram_diagram import HexagramDiagram

class HexagramWidget(QWidget):
    hexagramClicked = pyqtSignal(object)

    def __init__(self, hexagram=None, parent=None):
        super().__init__(parent)
        self.hexagram = hexagram
        layout = QVBoxLayout(self)
        layout.setSpacing(15)  # 增加间距

        self.diagram = HexagramDiagram(hexagram)
        # 不设置固定大小，让它能够自适应父控件的大小
        layout.addWidget(self.diagram, alignment=Qt.AlignmentFlag.AlignCenter)

        self.name_label = QLabel()
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setStyleSheet("font-size: 24px; color: #333;")  # 进一步增大字体
        self.name_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))  # 进一步增大字体
        layout.addWidget(self.name_label)

        # 移除固定大小设置，让控件能够根据内容自适应大小
        self.mousePressEvent = self.widget_clicked

        if hexagram:
            self.update_hexagram(hexagram)

    def update_hexagram(self, hexagram):
        self.hexagram = hexagram
        self.diagram.update_hexagram(hexagram)
        self.name_label.setText(hexagram.name)
        self.setToolTip(f"{hexagram.name} - {hexagram.description}")

    def widget_clicked(self, event):
        if self.hexagram:
            self.hexagramClicked.emit(self.hexagram)

    def sizeHint(self):
        return QSize(200, 300)  # 调整建议尺寸