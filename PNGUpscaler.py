from FileMover import FileMover
from PIL import Image
import tempfile
from io import BytesIO


class PNGUpscaler:
    def __init__(self, name, source_path, quality=60, dpi=300):
        self.name = name
        self.source_path = source_path + name
        self.quality = quality
        self.dpi = dpi
        self.buffer = BytesIO()
      
    def compress(self):
        print(f"Processing image '{self.name}' with quality={self.quality} and dpi={self.dpi}")

        image_resize = Image.open(self.source_path)
        image_resize.save(self.buffer,format='PNG', optimize=True, dpi=(self.dpi, self.dpi))
    
    def saveFile(self, destination_path):
        destination_path = destination_path + self.name
        with open(destination_path, 'wb') as out:
                out.write(self.buffer.getvalue())