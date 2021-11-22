input_folder="../gui/output/"

input_file = input_folder + "out.svg"
output_file = input_folder + "out.png"

from PySide2.QtSvg import *
from PySide2.QtGui import *

def convertSvgToPng(svgFilepath,pngFilepath,width):
    r=QSvgRenderer(svgFilepath)
    height=r.defaultSize().height()*width/r.defaultSize().width()
    i=QImage(width,height,QImage.Format_ARGB32)
    p=QPainter(i)
    r.render(p)
    i.save(pngFilepath)
    p.end()

convertSvgToPng(input_file, output_file, 2560)


##########################################################################


# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM

# drawing = svg2rlg(input_file)
# renderPM.drawToFile(drawing, output_file, fmt="PNG")

# ########################################################

# from cairosvg import svg2png
# svg_code = open(input_file, 'rt').read()
# svg2png(bytestring=svg_code,write_to=output_file)


# from wand.api import library
# import wand.color
# import wand.image

# with wand.image.Image() as image:
#     with wand.color.Color('transparent') as background_color:
#         library.MagickSetBackgroundColor(image.wand, 
#                                          background_color.resource) 
#     image.read(blob=input_file.read(), format="svg")
#     png_image = image.make_blob("png32")

# with open(output_file, "wb") as out:
#     out.write(png_image)

###############################################################################




