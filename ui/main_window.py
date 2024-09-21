from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QTextDocument
from ui.tab_64_hexagrams import Tab64Hexagrams
from ui.tab_hexagram_generator import TabHexagramGenerator
from ui.tab_hexagram_search import TabHexagramSearch

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("易经程序")
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # 创建一个水平布局来放置标签页和打印按钮
        self.top_layout = QHBoxLayout()
        self.layout.addLayout(self.top_layout)

        self.tabs = QTabWidget()
        self.top_layout.addWidget(self.tabs)

        # 添加打印按钮
        self.print_button = QPushButton("打印64卦")
        self.print_button.clicked.connect(self.print_64_hexagrams)
        self.top_layout.addWidget(self.print_button)

        self.tab1 = Tab64Hexagrams()
        self.tab2 = TabHexagramGenerator()
        self.tab3 = TabHexagramSearch()

        self.tabs.addTab(self.tab1, "64卦")
        self.tabs.addTab(self.tab2, "卦象生成")
        self.tabs.addTab(self.tab3, "卦象搜索")

    def print_64_hexagrams(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            document = QTextDocument()
            document.setHtml(self.tab1.get_printable_content())
            document.print(printer)  # 这里改为 print 而不是 print_