import sys
import os.path
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtCore import QSize, Qt
from detector.bboxes import predict

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui/design.ui', self)

        self.open = self.findChild(QtWidgets.QAction, 'open') # Find the button
        self.open.triggered.connect(self.openPressed) # Remember to pass the definition/method, not the return value!

        self.save = self.findChild(QtWidgets.QAction, 'save') # Find the button
        self.save.setShortcut("Ctrl+S")
        self.save.triggered.connect(self.savePressed) # Remember to pass the definition/method, not the return value!

        self.grayscale = self.findChild(QtWidgets.QAction, 'grayscale') # Find the button
        self.grayscale.triggered.connect(self.grayscalePressed) # Remember to pass the definition/method, not the return value!

        self.update = self.findChild(QtWidgets.QAction, 'update') # Find the button
        self.update.triggered.connect(self.updatePressed) # Remember to pass the definition/method, not the return value!

        self.imageLabel = self.findChild(QtWidgets.QLabel, 'label')
        self.fname = "temp.png"
        self.image = QImage("temp.png")

        self.show()

    def openPressed(self):
        # This is executed when the button is pressed
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.')[0]
        if os.path.isfile(self.fname):
            cvImg = predict(self.fname)
            height, width, channel = cvImg.shape
            bytesPerLine = 3 * width
            self.image = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
            image = self.image.scaled(self.width(), int(self.height()*0.95), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.imageLabel.resize(self.size())
            self.imageLabel.setPixmap(QPixmap(image))
            self.show()

    def resizeEvent(self, event):
        image = self.image.scaled(self.width(), int(self.height()*0.95), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.imageLabel.resize(self.size())
        self.imageLabel.setPixmap(QPixmap(image))
        self.show()

    def savePressed(self):
        # This is executed when the button is pressed
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', self.fname.split(".")[0] + '_prediction.png')
        self.image.save(name[0])

    def grayscalePressed(self):
        # This is executed when the button is pressed
        print('grayscale changed')

    def updatePressed(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
