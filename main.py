import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTranslator, QLocale
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    translator = QTranslator()
    translator.load(f"translations/iching_{QLocale.system().name()}")
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
