from PNGUpscaler import PNGUpscaler
from SVGToPNG import SVGtoPNG
import os

root_directory = "e:/ai-art/"
svg_inbox_directory = root_directory + "svg_inbox/"
png_inbox_directory = root_directory + "png_inbox/"
outbox_directory = root_directory + "outbox/"

for filename in os.listdir(svg_inbox_directory):
    if os.path.isfile(os.path.join(svg_inbox_directory, filename)):
        processor = SVGtoPNG(filename, svg_inbox_directory, png_inbox_directory, output_width=3600, output_height=3600)
        processor.convert()

for filename in os.listdir(png_inbox_directory):
    if os.path.isfile(os.path.join(png_inbox_directory, filename)):
        processor = PNGUpscaler(filename, png_inbox_directory, outbox_directory, quality=1)
        processor.compress()

