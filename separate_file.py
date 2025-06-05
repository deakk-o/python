import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mydesign import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.change_text)
        self.checkBox.clicked.connect(self.change_text)
        self.pushButton.clicked.connect(self.show_color_formula)

    def change_text(self):
        name = self.lineEdit.text()
        if self.checkBox.isChecked():
            self.label_5.setText("Amazing")
            self.label_6.setText(f"Hi {name}!")
            return

    def show_color_formula(self):
        if not self.checkBox.isChecked():
            self.label_4.setText("Please check the box to see the result.")
            return


        color = self.comboBox.currentText()
        formulas = {
            "Teal": "2x blue; 1x green",
            "Magenta": "red",
            "Violet": "2x blue; 1x red",
            "Mint green": "1x blue; 2x green",
            "Orange": "red; yellow",
            "Pink": "red",
            "Auburn": "1x red; 2x yellow"
        }

        formula = formulas.get(color)

        if self.radioButton.isChecked():
            self.label_4.setText(f"Mix: {formula} + black")
        elif self.radioButton_2.isChecked():
            self.label_4.setText(f"Mix: {formula} + white")
        else:
            self.label_4.setText(f"Mix: {formula}")

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())