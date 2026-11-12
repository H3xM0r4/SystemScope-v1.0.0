import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow, STYLE

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("SystemScope")
    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
