
from PyQt5 import QtCore, QtGui, QtWidgets


############ basic layout/GUI for the application #################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # main window parameters
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 716)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #main label area -> 'Please enter personal information' 
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 'Enter Name' field parameters
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 110, 211, 31))
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")

        # Label 'Name' parameters
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 56, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # 'Enter Surname' field parameters
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 180, 211, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Label 'Surname' parameters
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # 'Enter Date of Birth' field parameters
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 260, 211, 31))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")

        # Label 'Date of Birth' parameters
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 270, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # Label 'Upload ind...' parameters
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 370, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # push button 'Upload' parameters
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 370, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # push button 'Verify' parameters
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 520, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        # Label 'path_label' parameters
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(500, 375, 221, 21))
        self.path_label.setText("")
        self.path_label.setObjectName("path_label")

        #status bar label
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.path_label.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # naming function for layout properties
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZealID Pro"))
        self.label.setText(_translate("MainWindow", "Please enter personal information :"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Surname"))
        self.label_3.setText(_translate("MainWindow", "Surname:"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        self.label_4.setText(_translate("MainWindow", "Date of Birth:"))
        self.label_5.setText(_translate("MainWindow", "Upload indentification document:"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))
        self.pushButton_2.setText(_translate("MainWindow", "Verify"))
