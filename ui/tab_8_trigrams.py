from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QFont
from logic.trigram import Trigrams
import random

class TrigramDiagram(QWidget):
    def __init__(self, trigram, yang_color=QColor(255, 0, 0), parent=None):
        super().__init__(parent)
        self.trigram = trigram
        self.yang_color = yang_color
        self.yin_color = QColor(0, 0, 0)
        self.setFixedSize(80, 80)

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

        for i, bit in enumerate(self.trigram.binary):  # 移除 reversed
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

class Tab8Trigrams(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.trigrams = Trigrams.TRIGRAMS
        self.current_trigram = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)  # 增加整体布局的间距

        # 模式选择
        mode_layout = QHBoxLayout()
        self.mode_group = QButtonGroup(self)
        self.name_to_image_mode = QRadioButton("名称匹配图像")
        self.image_to_name_mode = QRadioButton("图像匹配名称")
        self.mode_group.addButton(self.name_to_image_mode)
        self.mode_group.addButton(self.image_to_name_mode)
        mode_layout.addWidget(self.name_to_image_mode)
        mode_layout.addWidget(self.image_to_name_mode)
        layout.addLayout(mode_layout)

        # 问题显示区域
        self.question_label = QLabel()
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(16)  # 增大字体大小
        font.setBold(True)
        self.question_label.setFont(font)
        layout.addWidget(self.question_label)

        # 答案选择区域
        self.answer_layout = QGridLayout()
        self.answer_layout.setSpacing(20)  # 增加卦象之间的距离
        layout.addLayout(self.answer_layout)

        # 结果显示
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(14)  # 增大结果字体大小
        self.result_label.setFont(font)
        layout.addWidget(self.result_label)

        # 下一题按钮
        self.next_button = QPushButton("下一题")
        self.next_button.clicked.connect(self.new_question)
        layout.addWidget(self.next_button)

        # 初始化
        self.name_to_image_mode.setChecked(True)
        self.new_question()

    def new_question(self):
        self.clear_layout(self.answer_layout)
        self.result_label.clear()
        self.current_trigram = random.choice(self.trigrams)

        if self.name_to_image_mode.isChecked():
            self.setup_name_to_image_question()
        else:
            self.setup_image_to_name_question()

    def setup_name_to_image_question(self):
        self.question_label.setText(f"请选择代表 '{self.current_trigram.name}' 的卦象：")
        options = random.sample(self.trigrams, 8)
        for i, trigram in enumerate(options):
            diagram = TrigramDiagram(trigram)
            button = QPushButton()
            button.setFixedSize(120, 120)  # 增大按钮大小
            layout = QVBoxLayout(button)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(diagram, alignment=Qt.AlignmentFlag.AlignCenter)
            button.clicked.connect(lambda checked, t=trigram: self.check_answer(t))
            self.answer_layout.addWidget(button, i // 4, i % 4)

    def setup_image_to_name_question(self):
        self.question_label.setText("请选择下面卦象的正确名称：")
        diagram = TrigramDiagram(self.current_trigram)
        diagram.setFixedSize(100, 100)  # 设置固定大小
        self.question_label.setLayout(QVBoxLayout())
        self.question_label.layout().addWidget(diagram, alignment=Qt.AlignmentFlag.AlignCenter)
        
        options = random.sample(self.trigrams, 8)
        for i, trigram in enumerate(options):
            button = QPushButton(trigram.name)
            button.setFixedSize(120, 60)  # 设置固定大小
            font = QFont()
            font.setPointSize(12)  # 增大按钮文字大小
            button.setFont(font)
            button.clicked.connect(lambda checked, t=trigram: self.check_answer(t))
            self.answer_layout.addWidget(button, i // 4, i % 4)

    def check_answer(self, selected_trigram):
        if selected_trigram.binary == self.current_trigram.binary:
            self.result_label.setText("回答正确！")
        else:
            self.result_label.setText(f"回答错误。正确答案是：{self.current_trigram.name}")

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()