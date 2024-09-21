import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter

from logic.trigram import Trigrams

class TrigramDisplayTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trigram Display Test")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 创建一个网格布局来显示 8 个卦象
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        # 获取所有的上卦或下卦
        self.trigrams = Trigrams.get_all_trigrams()

        # 在网格中添加每个卦象
        for i, trigram in enumerate(self.trigrams):
            trigram_widget = self.create_trigram_widget(trigram)
            row = i // 4
            col = i % 4
            grid_layout.addWidget(trigram_widget, row, col)

        # 添加一个切换按钮来在上卦和下卦之间切换
        self.toggle_button = QPushButton("切换上卦/下卦")
        self.toggle_button.clicked.connect(self.toggle_trigrams)
        main_layout.addWidget(self.toggle_button)

        self.is_upper = True  # 用于跟踪当前显示的是上卦还是下卦

    def create_trigram_widget(self, trigram):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # 创建一个自定义的 TrigramDiagram 来显示卦象
        diagram = TrigramDiagram(trigram)
        diagram.setFixedSize(100, 100)
        layout.addWidget(diagram)

        # 添加卦象名称标签
        name_label = QLabel(f"{trigram.name} ({trigram.nature})")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(name_label)

        return widget

    def toggle_trigrams(self):
        self.is_upper = not self.is_upper
        self.trigrams = Trigrams.get_all_trigrams(self.is_upper)
        
        # 更新所有卦象
        for i, trigram in enumerate(self.trigrams):
            item = self.centralWidget().layout().itemAt(0).layout().itemAt(i)
            if item:
                widget = item.widget()
                diagram = widget.layout().itemAt(0).widget()
                diagram.update_trigram(trigram)
                widget.layout().itemAt(1).widget().setText(f"{trigram.name} ({trigram.nature})")

        self.toggle_button.setText("切换到" + ("上卦" if self.is_upper else "下卦"))

class TrigramDiagram(QWidget):
    def __init__(self, trigram, yang_color=QColor(255, 0, 0), parent=None):
        super().__init__(parent)
        self.trigram = trigram
        self.yang_color = yang_color
        self.yin_color = QColor(0, 0, 0)

    def paintEvent(self, event):
        if not self.trigram:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        line_height = height // 4
        line_width = int(width * 0.8)
        x_start = int(width * 0.1)

        for i, bit in enumerate(reversed(self.trigram.binary)):
            y = height - (i + 1) * line_height
            if bit == '1':  # 阳爻
                painter.setBrush(self.yang_color)
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawRect(x_start, y, line_width, line_height // 2)
            else:  # 阴爻
                painter.setBrush(self.yin_color)
                painter.setPen(Qt.PenStyle.NoPen)
                half_width = line_width // 2 - 5
                painter.drawRect(x_start, y, half_width, line_height // 2)
                painter.drawRect(x_start + line_width - half_width, y, half_width, line_height // 2)

    def update_trigram(self, trigram):
        self.trigram = trigram
        self.update()

def main():
    app = QApplication(sys.argv)
    window = TrigramDisplayTestWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()