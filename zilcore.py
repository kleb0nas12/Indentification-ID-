import requests
from requests.exceptions import HTTPError
from widgets import ErrorBox
from key import api_key
import json
import base64
import hashlib


class CoreId:
    
    '''
    Class methods to handle and fetch data from the
    ZealID api endpoint.
    '''

    def __init__(self):
        self.err_handler = ErrorBox() #error message box


    def get_passport_data(self,image_loc,pass_type) -> str:  # validating and getting data from MRZ zone

        def _get_base64_sha1() -> tuple:  # transforming passport image to binary nad getting base64 and sha1 values
            with open(image_loc, 'rb') as img_file:
                file_bin = img_file.read()
                img_base64 = base64.b64encode(file_bin).decode('utf-8')
                img_sha1 = hashlib.sha1()
                img_sha1.update(file_bin)
            return img_base64, img_sha1.hexdigest()

        document, digest = _get_base64_sha1()

        # api request body
        url = 'https://api.identiway.com/docs/validate'
        head = {'x-api-key': api_key, 'Content-type': 'application/json'}
        data = {'document': document, 'digest': digest, 'type': pass_type}
        try:
            r = requests.post(url, data=json.dumps(data), headers=head)
            content = json.loads(r.content)
            return content.get('ocr_texts')[0]
        except requests.HTTPError as http_error:
            self.err_handler.show(f'HTTPError with status{r.status_code}',f'API call failed with reason: \n{http_error}')
        except Exception as e:
            self.err_handler.show('Exception has occured', f'API call failed due reasons: \nException error: {e}\n Message: {r.content}')


    def parse_data(self, data:str)-> dict: # parsing string data to get required elements (name,surname,bod, etc...)
        _data = data.split('\n')
        if len(_data) > 20:
            #type = Passport
            return {'Name': _data[12], 'Surname': _data[10],'DoB': _data[17],'country': _data[23],'gender':_data[22],'personal_code':_data[18]}  
        else:
            #type = Id_card  
            return {'Name': _data[5], 'Surname': _data[4],'DoB': _data[7],'country': _data[10],'gender':_data[9],'personal_code':_data[8]}  
           
