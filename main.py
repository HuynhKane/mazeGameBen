from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__ (self):
        super().__init__()
        button = QPushButton("Empty")
        button.clicked.connect(self.clicked_button)

        button2 = QPushButton("Empty")
        button2.clicked.connect(self.clicked_button)

        button3 = QPushButton("Empty")
        button3.clicked.connect(self.clicked_button)

        button4 = QPushButton("Empty")
        button4.clicked.connect(self.clicked_button)

        button5 = QPushButton("Empty")
        button5.clicked.connect(self.clicked_button)

        h1 = QHBoxLayout(self)
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()

        h1.addLayout(v1)
        h1.addLayout(v2)
        h1.addLayout(v3)

        v1.addWidget(button)
        v2.addWidget(button2)
        v3.addWidget(button3)
        V1.addWidget(button4)

        self.show()


    def clicked_button(self):
        button.setText("new text")
    
app = QApplication([])
win = Window()

app.exec()