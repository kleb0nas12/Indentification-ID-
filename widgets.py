from PyQt5.QtWidgets import QMessageBox


### Pyqt5 construct to output messages
class ErrorBox:

    # setting up and showing message box
    def show(self,title:str,message:str):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        _run = msg.exec_()
