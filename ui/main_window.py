from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QMenuBar, QMessageBox, QApplication
from PyQt6.QtCore import QTranslator, QLocale
from PyQt6.QtGui import QIcon, QAction
from ui.tab_64_hexagrams import Tab64Hexagrams
from ui.tab_hexagram_generator import TabHexagramGenerator
from ui.tab_hexagram_search import TabHexagramSearch
from ui.tab_8_trigrams import Tab8Trigrams

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.tr("I Ching"))
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

        self.tabs.addTab(self.tab1, self.tr("64 Hexagrams"))
        self.tabs.addTab(self.tab2, self.tr("Hexagram Generator"))
        self.tabs.addTab(self.tab3, self.tr("Hexagram Search"))
        self.tabs.addTab(self.tab_8_trigrams, self.tr("Eight Trigrams"))

        self.translator = QTranslator()
        self.current_language = 'zh'  # 默认语言设置为中文

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # File menu
        self.file_menu = menubar.addMenu(self.tr('File'))
        self.exit_action = QAction(self.tr('Exit'), self)
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)

        # Language menu
        self.language_menu = menubar.addMenu(self.tr('Language'))
        self.english_action = QAction('English', self)
        self.english_action.triggered.connect(lambda: self.change_language('en'))
        self.english_action.setCheckable(True)
        self.language_menu.addAction(self.english_action)

        self.chinese_action = QAction('中文', self)
        self.chinese_action.triggered.connect(lambda: self.change_language('zh'))
        self.chinese_action.setCheckable(True)
        self.language_menu.addAction(self.chinese_action)

        # 设置默认选中的语言
        self.update_language_menu()

        # Help menu
        self.help_menu = menubar.addMenu(self.tr('Help'))
        self.about_action = QAction(self.tr('About'), self)
        self.about_action.triggered.connect(self.show_about)
        self.help_menu.addAction(self.about_action)

    def update_language_menu(self):
        self.english_action.setChecked(self.current_language == 'en')
        self.chinese_action.setChecked(self.current_language == 'zh')

    def change_language(self, lang):
        self.current_language = lang
        self.translator = QTranslator()
        if self.translator.load(f"translations/iching_{lang}"):
            QApplication.instance().installTranslator(self.translator)
            self.retranslateUi()
            self.update_language_menu()
        else:
            print(f"Failed to load translation for {lang}")

    def retranslateUi(self):
        self.setWindowTitle(self.tr("I Ching"))
        self.tabs.setTabText(0, self.tr("64 Hexagrams"))
        self.tabs.setTabText(1, self.tr("Hexagram Generator"))
        self.tabs.setTabText(2, self.tr("Hexagram Search"))
        self.tabs.setTabText(3, self.tr("Eight Trigrams"))
        
        # Update menus
        self.file_menu.setTitle(self.tr('File'))
        self.language_menu.setTitle(self.tr('Language'))
        self.help_menu.setTitle(self.tr('Help'))
        self.exit_action.setText(self.tr('Exit'))
        self.about_action.setText(self.tr('About'))
        
        # Retranslate other components
        self.tab1.retranslateUi()
        self.tab2.retranslateUi()
        self.tab3.retranslateUi()
        self.tab_8_trigrams.retranslateUi()

    def show_about(self):
        QMessageBox.about(self, self.tr("About I Ching"),
                          self.tr("I Ching Application\n"
                                  "Version 1.0\n"
                                  "© 2023 Your Name/Company"))