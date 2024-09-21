from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QScrollArea
from PyQt6.QtCore import Qt
from ui.hexagram_widget import HexagramWidget

class HexagramDetailDialog(QDialog):
    def __init__(self, hexagram, parent=None):
        super().__init__(parent)
        self.hexagram = hexagram
        self.setWindowTitle(f"{hexagram.name} - 详细信息")
        self.setGeometry(100, 100, 600, 700)  # 增加对话框高度
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        # 添加卦象图和名称
        top_layout = QHBoxLayout()
        
        # 卦象图
        hexagram_widget = HexagramWidget(self.hexagram)
        hexagram_widget.setFixedSize(200, 200)  # 增加卦象图大小
        top_layout.addWidget(hexagram_widget)

        # 卦名和卦序
        name_layout = QVBoxLayout()
        name_label = QLabel(self.hexagram.name)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        number_label = QLabel(f"第 {self.hexagram.number} 卦")
        number_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_layout.addWidget(name_label)
        name_layout.addWidget(number_label)
        top_layout.addLayout(name_layout)

        main_layout.addLayout(top_layout)

        # 添加分隔线
        line = QWidget()
        line.setFixedHeight(2)
        line.setStyleSheet("background-color: #c0c0c0;")
        main_layout.addWidget(line)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        content_layout = QVBoxLayout(content_widget)

        # 添加卦辞
        self.add_info_row(content_layout, "卦辞", self.hexagram.description)

        # 添加卦的详细解释
        content_layout.addWidget(QLabel("卦辞解释:"))
        description_label = QLabel(self.hexagram.description)
        description_label.setWordWrap(True)
        description_label.setStyleSheet("padding: 10px; background-color: #f0f0f0; border-radius: 5px;")
        content_layout.addWidget(description_label)

        # 添加爻辞
        content_layout.addWidget(QLabel("爻辞:"))
        for i, line in enumerate(self.hexagram.lines, 1):
            self.add_info_row(content_layout, f"第{i}爻", line)

        main_layout.addWidget(scroll_area)

    def add_info_row(self, layout, label, value):
        row_layout = QHBoxLayout()
        label_widget = QLabel(f"{label}:")
        label_widget.setFixedWidth(80)
        row_layout.addWidget(label_widget)
        value_widget = QLabel(value)
        value_widget.setWordWrap(True)
        row_layout.addWidget(value_widget)
        layout.addLayout(row_layout)