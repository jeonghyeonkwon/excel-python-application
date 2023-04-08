import sys
from PyQt6.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        button_1 = QPushButton("따옴표 붙이기")
        

        layout.addWidget(button_1)
        

        self.setLayout(layout)
        self.setGeometry(100,300,1000, 500)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec())