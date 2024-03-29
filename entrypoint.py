from SVGToPNG import SVGtoPNG
from Vectorizer import Vectorizer
import os


root_directory = "e:/ai-art/0000_proc/"
base_inbox_directory = root_directory +"base_inbox/"
svg_inbox_directory = root_directory + "svg_inbox/"
png_inbox_directory = root_directory + "png_inbox/"
outbox_directory = root_directory + "outbox/"

#for filename in os.listdir(base_inbox_directory):
#    if os.path.isfile(os.path.join(base_inbox_directory, filename)):
#        processor = Vectorizer(filename, base_inbox_directory)
#        processor.vectorize()
#        processor.saveFile("")

for filename in os.listdir(svg_inbox_directory):
    if os.path.isfile(os.path.join(svg_inbox_directory, filename)):
        processor = SVGtoPNG(filename, svg_inbox_directory, output_width=3600, output_height=3600, quality = 1)
        processor.convert()
        processor.compress()
        processor.saveFile("")
