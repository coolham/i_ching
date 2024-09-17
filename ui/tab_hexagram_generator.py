from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from logic.iching import IChing
from ui.hexagram_widget import HexagramWidget

class TabHexagramGenerator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(30)  # 增加垂直间距

        self.result_widget = HexagramWidget(None)
        self.result_widget.setFixedSize(400, 600)  # 进一步增大卦象显示尺寸
        layout.addWidget(self.result_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.description_label = QLabel()
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("font-size: 28px; margin-top: 40px;")  # 进一步增大字体大小
        layout.addWidget(self.description_label)

        generate_button = QPushButton("生成卦象")
        generate_button.setStyleSheet("font-size: 28px; padding: 20px;")  # 进一步增大按钮字体和内边距
        generate_button.clicked.connect(self.generate_hexagram)
        layout.addWidget(generate_button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(1)  # 添加弹性空间，使控件集中在顶部

    def generate_hexagram(self):
        hexagram = IChing.generate_random_hexagram()
        self.result_widget.update_hexagram(hexagram)
        self.description_label.setText(f"{hexagram.name} - {hexagram.mnemonic}\n\n{hexagram.description}")