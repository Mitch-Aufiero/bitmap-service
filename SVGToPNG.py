from FileExtensionReplacer import FileExtensionReplacer
import cairosvg
from io import BytesIO
from PIL import Image


class SVGtoPNG:
    def __init__(self, name, source_path, output_width, output_height, quality=60, dpi=300):
        self.name = name
        self.source_path = source_path + name
        self.output_width = output_width
        self.output_height = output_height
        self.quality = quality
        self.dpi = dpi
        self.buffer = BytesIO()

    def convert(self):
        print(f"Converting image '{self.name}' with output_width={self.output_width} and output_height={self.output_height}")
        cairosvg.svg2png(url=self.source_path, write_to=self.buffer, output_width=self.output_width, output_height=self.output_height)
 
    
    def compress(self):
        print(f"Processing image '{self.name}' with quality={self.quality} and dpi={self.dpi}")

        image_resize = Image.open(self.buffer)
        self.buffer = BytesIO()
        image_resize.save(self.buffer,format='PNG', optimize=True, dpi=(self.dpi, self.dpi))

    
    def saveFile(self, destination_path):
        destination_path = destination_path + FileExtensionReplacer.replace_file_extension(self.name, ".png")
        with open(destination_path, 'wb') as out:
                out.write(self.buffer.getvalue())

