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
        self.name_to_image_mode = QRadioButton(self.tr("Name to Image"))
        self.image_to_name_mode = QRadioButton(self.tr("Image to Name"))
        self.mode_group.addButton(self.name_to_image_mode)
        self.mode_group.addButton(self.image_to_name_mode)
        mode_layout.addWidget(self.name_to_image_mode)
        mode_layout.addWidget(self.image_to_name_mode)
        layout.addLayout(mode_layout)

        # 连接模式切换信号
        self.mode_group.buttonClicked.connect(self.new_question)

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
        # 移除旧的问题部件（如果存在）
        if hasattr(self, 'question_widget'):
            self.layout().removeWidget(self.question_widget)
            self.question_widget.deleteLater()
            del self.question_widget

        self.clear_layout(self.answer_layout)
        self.result_label.clear()
        self.current_trigram = random.choice(self.trigrams)

        if self.name_to_image_mode.isChecked():
            self.setup_name_to_image_question()
        else:
            self.setup_image_to_name_question()

    def setup_name_to_image_question(self):
        self.question_label.setText(self.tr(f"Please select the trigram for '{self.current_trigram.name}':"))
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
        self.question_widget = QWidget()
        question_layout = QVBoxLayout(self.question_widget)
        
        # 添加卦象图
        diagram = TrigramDiagram(self.current_trigram)
        diagram.setFixedSize(100, 100)
        question_layout.addWidget(diagram, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 添加问题文本
        question_text = QLabel(self.tr("What is the name of this trigram?"))
        question_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        question_text.setFont(QFont("Arial", 14))
        question_layout.addWidget(question_text)
        
        # 将问题部件添加到主布局
        self.layout().insertWidget(1, self.question_widget)
        
        # 创建答案按钮
        options = random.sample(self.trigrams, 8)
        for i, trigram in enumerate(options):
            button = QPushButton(f"{trigram.name} ({trigram.nature})")
            button.setFixedSize(150, 60)  # 增加按钮大小以容纳更多文本
            font = QFont()
            font.setPointSize(12)
            button.setFont(font)
            button.clicked.connect(lambda checked, t=trigram: self.check_answer(t))
            self.answer_layout.addWidget(button, i // 4, i % 4)

    def check_answer(self, selected_trigram):
        if selected_trigram.binary == self.current_trigram.binary:
            self.result_label.setText(self.tr("Correct answer!"))
        else:
            self.result_label.setText(self.tr(f"Wrong answer. The correct answer is: {self.current_trigram.name} ({self.current_trigram.nature})"))

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def retranslateUi(self):
        self.name_to_image_mode.setText(self.tr("Name to Image"))
        self.image_to_name_mode.setText(self.tr("Image to Name"))
        self.next_button.setText(self.tr("Next Question"))
        # 更新其他任何需要翻译的文本元素