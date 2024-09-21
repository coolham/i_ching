import sys
import os
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QSize, QRectF
from PyQt6.QtGui import QColor, QPainter, QFont
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from logic.iching import IChing
from ui.hexagram_diagram import HexagramDiagram
from ui.hexagram_print_service import HexagramPrintService

class HexagramDiagramTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hexagram Diagram Test")
        self.setGeometry(100, 100, 300, 750)  # 增加窗口高度

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 确保 HEXAGRAMS 是一个列表
        self.hexagrams = list(IChing.HEXAGRAMS)

        # 创建 HexagramDiagram，并明确指定 yang_color
        yang_color = QColor(255, 0, 0)  # 定义阳爻颜色为红色
        self.hexagram_diagram = HexagramDiagram(yang_color=yang_color)
        self.hexagram_diagram.setFixedSize(250, 400)  # 增加大小以便更好地观察

        layout.addWidget(self.hexagram_diagram, alignment=Qt.AlignmentFlag.AlignCenter)

        # 添加卦象信息标签
        self.info_label = QLabel()
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        # 添加一个按钮来随机选择新的卦象
        self.random_button = QPushButton("随机选择卦象")
        self.random_button.clicked.connect(self.select_random_hexagram)
        layout.addWidget(self.random_button)

        # 添加打印按钮
        self.print_button = QPushButton("打印当前卦象")
        self.print_button.clicked.connect(self.print_hexagram)
        layout.addWidget(self.print_button)

        self.select_random_hexagram()
        self.print_service = HexagramPrintService()

    def select_random_hexagram(self):
        random_hexagram = random.choice(self.hexagrams)
        self.hexagram_diagram.update_hexagram(random_hexagram)
        self.update_hexagram_info(random_hexagram)
        self.hexagram_diagram.update()  # 强制更新卦象图

    def update_hexagram_info(self, hexagram):
        info_text = f"卦名: {hexagram.name}\n"
        info_text += f"序号: {hexagram.number}\n"
        info_text += f"二进制: {hexagram.binary}\n"
        info_text += f"符号: {hexagram.symbol}\n"
        info_text += f"助记词: {hexagram.mnemonic}\n"
        info_text += f"宫位: {hexagram.palace}\n"
        info_text += f"描述: {hexagram.description}\n"
        self.info_label.setText(info_text)

    def print_hexagram(self):
        if self.hexagram_diagram.hexagram:
            self.print_service.print_hexagram(self.hexagram_diagram.hexagram, self)

def main():
    app = QApplication(sys.argv)
    window = HexagramDiagramTestWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()