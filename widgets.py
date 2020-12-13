from PyQt5.QtWidgets import QMessageBox

class ErrorBox:

    def show(self,title:str,message:str):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        _run = msg.exec_()
