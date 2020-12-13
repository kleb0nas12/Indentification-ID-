import sys
import re
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
from layout import Ui_MainWindow
from widgets import ErrorBox
from zilcore import CoreId
from PyQt5 import QtGui




class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow() # layout access
        self.ui.setupUi(self.main_win)
        self.zil_core = CoreId() # ZilID access
        self.err_box = ErrorBox() #error message box
        self.doc_path = None #document path location


        ### UI functionality ###
        self.ui.pushButton.clicked.connect(self.get_img_path) # Upload button functionality
        self.ui.pushButton_2.clicked.connect(self.verification) # executing main verification process -> clicked on verification button 

    ### UI elements' func methods ###

    # getting file path from the backend
    def get_img_path(self):
        file_path = QFileDialog.getOpenFileName() # getting file path 
        self.doc_path = file_path[0]
        file_id = file_path[0].split('/')[-1] # getting file name from the path string
        self.ui.path_label.setText(file_id) # showing file name in the application after 'upload' button is clicked
    
    # method to check validity of entered data and main process execution
    def verification(self):

        ## Verification of input data ##
        def _check_name(name: str)-> bool: #method to check if name is valid (only type of letters)
            if name.isalpha():
                return True
            return False

        def _check_surname(surname: str)-> bool: #method to check if surname is valid (only type of letters)
            if surname.isalpha():
                return True
            return False

        def _check_dob(dob: str)->bool: # regular expression method to check if provided date of birth (dob) matches pattern (YYYY-MM-DD)
            pattern = re.match('^(19[0-9][0-9]|20[0-9][0-9])(-)(0[1-9]|1[0-2])(-)(0[1-9]|1[0-9])|2[0-9]|3[0-1]$', dob)
            if pattern:
                return True
            return False

        def _exec_check(): # Executing check and returning values
            name = self.ui.lineEdit.text() # name value from name_field
            surname = self.ui.lineEdit_2.text()  # surname value from surname_field
            dob = self.ui.lineEdit_3.text() # date of birth value from dob_field

            return _check_name(name),_check_surname(surname), _check_dob(dob)
        
        ##

        text_values= _exec_check() #getting logical values of input validity -> tuple(True/False)

        if False in text_values: # if info was not provided correctly , returning error message box with fields to check and correct
            _text = '' #error message text
            if text_values[0] == False:
                _text = _text +'\n - Name (only letters)'
            if text_values[1] == False:
                _text = _text +'\n - Surname (only letters)' 
            if text_values[2] == False:
                _text = _text +'\n - Date of Birth (format YYYY-MM-DD)'

            _error_message = f'Please correct the fields: \n {_text}'

            self.err_box.show('Input Error',_error_message) # error message box
        else:
            output_data = self.zil_core.get_passport_data(self.doc_path,'lt_pass_rev') # executing ZilId api request
            if output_data is None: #if request failed
                pass # exception has occured during request execution and was raised by CoreId class' module
            else:
                _doc_data = self.zil_core.parse_data(output_data)
                print(_doc_data)




        

    #  method to show output
    def show_main(self):
        self.main_win.show()




if __name__ == '__main__':
    # application setup
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show_main()
    sys.exit(app.exec_())