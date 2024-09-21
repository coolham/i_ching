from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea
from PyQt6.QtCore import Qt
from logic.iching import IChing
from ui.hexagram_widget import HexagramWidget

class TabHexagramSearch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setStyleSheet("font-size: 16px;")  # 增大输入框字体
        self.search_button = QPushButton(self.tr("Search"))
        self.search_button.setStyleSheet("font-size: 16px;")  # 增大按钮字体
        self.search_button.clicked.connect(self.search_hexagrams)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        self.search_results = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_content.setLayout(self.search_results)
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

    def search_hexagrams(self):
        keyword = self.search_input.text()
        results = IChing.search_hexagram(keyword)
        
        # 清除之前的搜索结果
        for i in reversed(range(self.search_results.count())): 
            self.search_results.itemAt(i).widget().setParent(None)
        
        if results:
            for hexagram in results:
                result_widget = HexagramWidget(hexagram)
                self.search_results.addWidget(result_widget)
        else:
            no_result_label = QLabel(self.tr("No matching hexagrams found"))
            no_result_label.setStyleSheet("font-size: 16px;")
            self.search_results.addWidget(no_result_label)

    def retranslateUi(self):
        self.search_button.setText(self.tr("Search"))
        # 更新其他任何需要翻译的文本元素