from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.setWindowTitle("CADENCE COUNTER")

        self.layout = QHBoxLayout()

        self.label = QLabel(str(self.counter))
        self.layout.addWidget(self.label)

        self.button_layout = QVBoxLayout()

        self.inc_button = QPushButton("+")
        self.inc_button.clicked.connect(self.increment)
        self.button_layout.addWidget(self.inc_button)

        self.clear_button = QPushButton("clear")
        self.clear_button.clicked.connect(self.clear)
        self.button_layout.addWidget(self.clear_button)

        self.dec_button = QPushButton("-")
        self.dec_button.clicked.connect(self.decrement)
        self.button_layout.addWidget(self.dec_button)

        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

    def increment(self):
        self.counter += 1
        self.label.setText(str(self.counter))

    def clear(self):
        self.counter = 0
        self.label.setText(str(self.counter))

    def decrement(self):
        self.counter -= 1
        self.label.setText(str(self.counter))


app = QApplication([])
window = CounterApp()
window.show()
app.exec_()

