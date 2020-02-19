
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def pictureone(self):
        self.picture.setPixmap(QtGui.QPixmap("Screenshot from 2020-01-04 02-27-04.png"))

    def picturetwo(self):
        self.picture.setPixmap(QtGui.QPixmap("images.png"))

    def picturethree(self):
        self.picture.setPixmap(QtGui.QPixmap("Screenshot from 2020-01-28 13-55-45.png"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(0, 0, 811, 511))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("Screenshot from 2020-01-04 02-27-04.png"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.picture1 = QtWidgets.QPushButton(self.centralwidget)
        self.picture1.setGeometry(QtCore.QRect(0, 510, 271, 41))
        self.picture1.setObjectName("picture1")
        self.picture2 = QtWidgets.QPushButton(self.centralwidget)
        self.picture2.setGeometry(QtCore.QRect(270, 510, 261, 41))
        self.picture2.setObjectName("picture2")
        self.picture3 = QtWidgets.QPushButton(self.centralwidget)
        self.picture3.setGeometry(QtCore.QRect(530, 510, 271, 41))
        self.picture3.setObjectName("picture3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.picture1.clicked.connect(self.pictureone)
        self.picture2.clicked.connect(self.picturetwo)
        self.picture3.clicked.connect(self.picturethree)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picture1.setText(_translate("MainWindow", "picture one"))
        self.picture2.setText(_translate("MainWindow", "picture two"))
        self.picture3.setText(_translate("MainWindow", "picture three"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
