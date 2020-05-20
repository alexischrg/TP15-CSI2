from PySide2.QtWidgets import *

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)

        self.layout = QVBoxLayout()

        self.buttonsPanel = ButtonsPanel()
        self.notificationPanel = QTextEdit()
        self.resultTable = QTableWidget(5,3)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonsPanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resultTable)

        self.setLayout(self.layout)


class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.buttonA = QPushButton("Configure")
        self.buttonB = QPushButton("Connect")
        self.buttonC = QPushButton("Disconnect")

        self.layout.addWidget(self.buttonA)
        self.layout.addWidget(self.buttonB)
        self.layout.addWidget(self.buttonC)

        self.setLayout(self.layout)
class LabeledTextField(QWidget):
    def __init__(self,a):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.label = QLabel(a)
        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(20)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration")
        self.layout = QVBoxLayout()

        self.A = LabeledTextField("IPaddress")
        self.B = LabeledTextField("User")
        self.C = LabeledTextField("Password")

        self.layout.addWidget(self.A)
        self.layout.addWidget(self.B)
        self.layout.addWidget(self.C)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = ConfigurationDialog()
    win2 = SQLClientWindow()
    win.show()
    win2.show()
    app.exec_()