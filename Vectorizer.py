from FileExtensionReplacer import FileExtensionReplacer
import requests
import configparser
from io import BytesIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage


class Vectorizer:
    def __init__(self, name, source_path):
        self.name = name
        self.source_path = source_path + name
        self.buffer = BytesIO()

    def vectorize(self):
        print(f"Vectorizing image '{self.name}' ...")

        config = configparser.ConfigParser()
        config.read('config.ini')

        api_key=config.get('Keys', 'vectorizer_key')

        response = requests.post(
            'https://vectorizer.ai/api/v1/vectorize',
            files={'image': open(self.source_path, 'rb')},
            headers={
                'Authorization':
                'Basic ' + api_key
            },
        )
        if response.status_code == requests.codes.ok:
            # Save result
            self.buffer = response.content
        else:
            print("Error:", response.status_code, response.text)
    
    
    def saveFile(self, destination_path):
        destination_path = destination_path + FileExtensionReplacer.replace_file_extension(self.name, ".svg")

        config = configparser.ConfigParser()
        config.read('config.ini')

        cred = credentials.Certificate("serviceaccount.json")
        firebase_admin.initialize_app( cred, options ={'storageBucket': 'scrapbooking-ai.appspot.com'})

        bucket = storage.bucket()

        self.buffer.seek(0)
        blob = bucket.blob(destination_path)
        blob.upload_from_file(self.buffer)

        #destination_path = destination_path + FileExtensionReplacer.replace_file_extension(self.name, ".svg")
        #with open(destination_path, 'wb') as out:
        #        out.write(self.buffer)
