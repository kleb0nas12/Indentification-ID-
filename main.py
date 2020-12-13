import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from layout import Ui_MainWindow




class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

    #  method to show output
    def show_main(self):
        self.main_win.show()



if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show_main()
    sys.exit(app.exec_())