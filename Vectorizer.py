from FileExtensionReplacer import FileExtensionReplacer
import requests
import configparser
from io import BytesIO

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
        with open(destination_path, 'wb') as out:
                out.write(self.buffer)
