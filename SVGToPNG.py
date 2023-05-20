from FileExtensionReplacer import FileExtensionReplacer
import cairosvg
from io import BytesIO


class SVGtoPNG:
    def __init__(self, name, source_path, output_width, output_height):
        self.name = name
        self.source_path = source_path + name
        self.output_width = output_width
        self.output_height = output_height
        self.buffer = BytesIO()

    def convert(self):
        print(f"Converting image '{self.name}' with output_width={self.output_width} and output_height={self.output_height}")
        cairosvg.svg2png(url=self.source_path, write_to=self.buffer, output_width=self.output_width, output_height=self.output_height)

    
    def saveFile(self, destination_path):
        destination_path = destination_path + FileExtensionReplacer.replace_file_extension(self.name, ".png")
        with open(destination_path, 'wb') as out:
                out.write(self.buffer.getvalue())

