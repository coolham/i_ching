from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QScrollArea, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QTextDocument
from logic.iching import IChing
from ui.hexagram_widget import HexagramWidget
from ui.hexagram_detail_dialog import HexagramDetailDialog

class Tab64Hexagrams(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hexagrams = IChing.HEXAGRAMS
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # 添加打印按钮
        self.print_button = QPushButton("打印64卦")
        self.print_button.clicked.connect(self.print_64_hexagrams)
        layout.addWidget(self.print_button)

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
                index = (i * 8 + j)
                if 0 <= index < len(hexagrams):
                    hexagram = hexagrams[index]
                    hexagram_widget = HexagramWidget(hexagram)
                    hexagram_widget.setMinimumSize(80, 120)  # 设置最小大小
                    hexagram_widget.hexagramClicked.connect(self.on_hexagram_clicked)
                    grid_layout.addWidget(hexagram_widget, i, j)

    def on_hexagram_clicked(self, hexagram):
        dialog = HexagramDetailDialog(hexagram, self)
        dialog.exec()

    def get_printable_content(self):
        content = "<h1>64卦</h1>"
        for hexagram in self.hexagrams:
            content += f"<h2>{hexagram.name}</h2>"
            content += f"<p>卦象：{''.join(['▅▅' if line else '▅▅ ▅▅' for line in hexagram.lines])}</p>"
            content += f"<p>卦辞：{hexagram.description}</p>"
            content += "<hr>"
        return content

    def print_64_hexagrams(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            document = QTextDocument()
            document.setHtml(self.get_printable_content())
            document.print(printer)