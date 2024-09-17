from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTextEdit, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from ui.hexagram_diagram import HexagramDiagram

class HexagramDetailDialog(QDialog):
    def __init__(self, hexagram, parent=None):
        super().__init__(parent)
        self.hexagram = hexagram
        self.setWindowTitle(f"{hexagram.name} - 详细信息")
        self.setMinimumSize(500, 700)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)  # 减小整体间距
        layout.setContentsMargins(20, 10, 20, 20)  # 减小上边距

        # 卦象图和名称
        diagram_widget = QWidget()
        diagram_layout = QVBoxLayout(diagram_widget)
        diagram_layout.setSpacing(5)  # 减小卦象和名称之间的间距
        diagram_layout.setContentsMargins(0, 0, 0, 0)  # 移除内边距

        self.hexagram_diagram = HexagramDiagram(hexagram)
        self.hexagram_diagram.setFixedSize(200, 300)  # 保持卦象图尺寸不变
        diagram_layout.addWidget(self.hexagram_diagram, alignment=Qt.AlignmentFlag.AlignCenter)

        # 卦名和符号
        name_label = QLabel(f"{hexagram.name} ({hexagram.symbol})")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        diagram_layout.addWidget(name_label)

        layout.addWidget(diagram_widget)

        # 其他信息
        info_text = f"序号: {hexagram.number}\n"
        info_text += f"二进制: {hexagram.binary}\n"
        info_text += f"助记词: {hexagram.mnemonic}\n"
        info_text += f"宫位: {hexagram.palace}\n"
        info_text += f"描述: {hexagram.description}\n\n"
        info_text += f"卦辞: {hexagram.judgment}\n\n"
        info_text += f"象辞: {hexagram.image}\n\n"
        info_text += "爻辞:\n" + "\n".join(hexagram.lines)

        info_edit = QTextEdit()
        info_edit.setPlainText(info_text)
        info_edit.setReadOnly(True)
        info_edit.setFont(QFont("Arial", 12))
        layout.addWidget(info_edit)

        self.setLayout(layout)