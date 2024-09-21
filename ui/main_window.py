from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from ui.tab_64_hexagrams import Tab64Hexagrams
from ui.tab_hexagram_generator import TabHexagramGenerator
from ui.tab_hexagram_search import TabHexagramSearch
from ui.tab_8_trigrams import Tab8Trigrams

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("易经")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        self.tab1 = Tab64Hexagrams()
        self.tab2 = TabHexagramGenerator()
        self.tab3 = TabHexagramSearch()
        self.tab_8_trigrams = Tab8Trigrams()

        self.tabs.addTab(self.tab1, "64卦")
        self.tabs.addTab(self.tab2, "卦象生成")
        self.tabs.addTab(self.tab3, "卦象搜索")
        self.tabs.addTab(self.tab_8_trigrams, "八卦")