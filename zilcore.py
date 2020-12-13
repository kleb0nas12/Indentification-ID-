import requests
from requests.exceptions import HTTPError
from key import api_key
import json
import base64
import hashlib


class CoreId:
    '''
    Class methods to handle and fetch data from the
    ZealID api endpoint.
    '''

    def get_passport_data(self,image_loc,pass_type) -> str:  # validating  getting data from MRZ zone

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
            print(http_error)
            # raise pop up window with error
        except Exception as e:
            print(e)
            # raise pop up windiw
