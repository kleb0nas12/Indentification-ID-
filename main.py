import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from layout import Ui_MainWindow
from zilcore import CoreId
from PyQt5 import QtGui




class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow() # layout access
        self.ui.setupUi(self.main_win)
        self.zil_core = CoreId() # ZIlId access


        ### UI functionality ###
        self.ui.pushButton.clicked.connect(self.get_img_url)


    def get_img_url(self):
        file_path = QFileDialog.getOpenFileName()
        print(file_path)

    #  method to show output
    def show_main(self):
        self.main_win.show()



if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show_main()
    sys.exit(app.exec_())