from FileExtensionReplacer import FileExtensionReplacer
import cairosvg


class SVGtoPNG:
    def __init__(self, name, source_path, destination_path, output_width, output_height):
        self.name = name
        self.source_path = source_path + name
        self.destination_path = destination_path + FileExtensionReplacer.replace_file_extension(name, ".png")
        self.output_width = output_width
        self.output_height = output_height

    def convert(self):
        print(f"Converting image '{self.name}' with output_width={self.output_width} and output_height={self.output_height}")
        cairosvg.svg2png(url=self.source_path, write_to=self.destination_path, output_width=self.output_width, output_height=self.output_height)

