from PIL import Image
import os

infile = 'image/kirby.jpg'
outfile = 'image/kirby_L.jpg'

pil_im = Image.open(infile).convert('L')

pil_im.save(outfile)


