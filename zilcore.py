import requests
from key import api_key
import json
import base64
import hashlib


class CoreId:

    def __init__(self, pass_type : str, image_loc : str):
        self.pass_type = pass_type
        self.image_loc = image_loc

    def get_passport_data(self)->str:

        def _get_base64_sha1() -> tuple:
            with open(self.image_loc, 'rb') as img_file:
                file_bin = img_file.read()
                img_base64 = base64.b64encode(file_bin).decode('utf-8')
                img_sha1 = hashlib.sha1()
                img_sha1.update(file_bin)
            return img_base64, img_sha1.hexdigest()

        document, digest = _get_base64_sha1()
        url = 'https://api.identiway.com/docs/validate'
        head = {'x-api-key': api_key, 'Content-type': 'application/json'}
        data = {'document': document, 'digest': digest, 'type': self.pass_type}

        r = requests.post(url, data=json.dumps(data), headers=head)
        content = json.loads(r.content)
        return content.get('ocr_texts')[0]


docu = R'A:\documents\lt_pass1.jpg'

x = CoreId('lt_pass_rev', docu).get_passport_data()
print(type(x))


for line in x:
    print(line)