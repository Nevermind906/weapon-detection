import sys
import os.path
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui/design.ui', self)

        self.open = self.findChild(QtWidgets.QAction, 'open') # Find the button
        self.open.triggered.connect(self.openPressed) # Remember to pass the definition/method, not the return value!

        self.save = self.findChild(QtWidgets.QAction, 'save') # Find the button
        self.save.triggered.connect(self.savePressed) # Remember to pass the definition/method, not the return value!

        self.grayscale = self.findChild(QtWidgets.QAction, 'grayscale') # Find the button
        self.grayscale.triggered.connect(self.grayscalePressed) # Remember to pass the definition/method, not the return value!

        self.update = self.findChild(QtWidgets.QAction, 'update') # Find the button
        self.update.triggered.connect(self.updatePressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def openPressed(self):
        # This is executed when the button is pressed
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.')[0]
        print(fname)
        if os.path.isfile(fname):
            self.image = QImage(fname)              # resize Image to widgets size
            sImage = self.image.scaled(QSize(800,600), Qt.KeepAspectRatio)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)

            self.label = QtWidgets.QLabel('Test', self)                        # test, if it's really backgroundimage
            self.label.setGeometry(50,50,200,50)
            self.show()

    def savePressed(self):
        # This is executed when the button is pressed
        print('Saving file')

    def grayscalePressed(self):
        # This is executed when the button is pressed
        print('grayscale changed')

    def updatePressed(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
