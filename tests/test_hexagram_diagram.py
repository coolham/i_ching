import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QComboBox, QLabel, QFrame
from PyQt6.QtCore import Qt
from logic.iching import IChing
from ui.hexagram_widget import HexagramWidget

class HexagramDiagramTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("卦象图示测试窗口")
        self.setGeometry(100, 100, 800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # 左侧布局
        left_widget = QFrame()
        left_widget.setFrameShape(QFrame.Shape.Box)
        left_widget.setLineWidth(2)
        left_widget.setStyleSheet("QFrame { border: 2px solid black; }")
        left_layout = QVBoxLayout(left_widget)
        self.hexagram_widget = HexagramWidget(None)
        self.hexagram_widget.setFixedSize(200, 300)  # 设置固定大小
        left_layout.addWidget(self.hexagram_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(left_widget)

        # 右侧布局
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        self.hexagram_selector = QComboBox()
        self.hexagram_selector.addItems([f"{h.number}-{h.name}（{h.mnemonic}）" for h in IChing.HEXAGRAMS])
        self.hexagram_selector.currentIndexChanged.connect(self.update_hexagram_display)
        right_layout.addWidget(self.hexagram_selector)

        self.hexagram_info = QLabel()
        self.hexagram_info.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.hexagram_info.setWordWrap(True)
        right_layout.addWidget(self.hexagram_info)

        right_layout.addStretch()
        main_layout.addWidget(right_widget)

        self.update_hexagram_display(0)

    def update_hexagram_display(self, index):
        hexagram = IChing.HEXAGRAMS[index]
        self.hexagram_widget.update_hexagram(hexagram)
        info_text = f"卦名: {hexagram.name}\n"
        info_text += f"序号: {hexagram.number}\n"
        info_text += f"二进制: {hexagram.binary}\n"
        info_text += f"符号: {hexagram.symbol}\n"
        info_text += f"助记词: {hexagram.mnemonic}\n"
        info_text += f"宫位: {hexagram.palace}\n"
        info_text += f"描述: {hexagram.description}\n"
        self.hexagram_info.setText(info_text)

def run_test():
    app = QApplication(sys.argv)
    window = HexagramDiagramTestWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_test()