from FileMover import FileMover
from PIL import Image
import tempfile


class PNGUpscaler:
    def __init__(self, name, source_path, destination_path, quality=60, dpi=300):
        self.name = name
        self.source_path = source_path + name
        self.destination_path = destination_path + name
        self.quality = quality
        self.dpi = dpi
      
    def compress(self):
        print(f"Processing image '{self.name}' with quality={self.quality} and dpi={self.dpi}")

        image_resize = Image.open(self.source_path)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        temp_filename = temp_file.name
        image_resize.save(temp_filename, optimize=True, dpi=(self.dpi, self.dpi))
        FileMover.move_file(temp_filename, self.destination_path)
        return