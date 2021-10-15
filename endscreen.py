import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class EndWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        centralwidget = QWidget()
        self.buttonLayout = QHBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.resumebutton = QPushButton()
        self.resumebutton.setText("Resume")
        self.resumebutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.buttonLayout.addWidget(self.resumebutton)

        self.settingbutton = QPushButton()
        self.settingbutton.setText("Settings")
        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.buttonLayout.addWidget(self.settingbutton)

        self.exitbutton = QPushButton()
        self.exitbutton.setText("Exit")
        self.exitbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.exitbutton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitbutton)

        centralwidget.setLayout(self.buttonLayout)
        self.setCentralWidget(centralwidget)

        self.scene = QGraphicsScene(-50, -50, 600, 600)

    def exitClicked(self, event):
        sys.exit(app)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PauseWindow()
    window.show()

    app.exec()