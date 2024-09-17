from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt
from logic.iching import IChing
from ui.hexagram_widget import HexagramWidget
from ui.hexagram_detail_dialog import HexagramDetailDialog

class Tab64Hexagrams(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        grid_layout = QGridLayout(scroll_content)
        grid_layout.setSpacing(10)  # 添加一些间距

        hexagrams = IChing.HEXAGRAMS
        for i in range(8):
            for j in range(8):
                index = 63 - (i * 8 + j)
                if 0 <= index < len(hexagrams):
                    hexagram = hexagrams[index]
                    hexagram_widget = HexagramWidget(hexagram)
                    hexagram_widget.hexagramClicked.connect(self.on_hexagram_clicked)
                    grid_layout.addWidget(hexagram_widget, i, j)

    def on_hexagram_clicked(self, hexagram):
        dialog = HexagramDetailDialog(hexagram, self)
        dialog.exec()