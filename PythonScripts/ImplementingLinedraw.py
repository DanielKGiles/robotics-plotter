import cv2
import linedraw

# import os
# cwd = os.getcwd()
# print("IMPLEMENTING LINEDRAW CURRENT WORKING DIRECTORY")
# print(cwd)

from math import *
import sys
sys.path.append('../PythonScripts/')
import plotter
import pickle
import SendDataToPi
import VisualizeLines
from ScalingImages import scale_image

# The following two packages are needed for converting SVG to PNG
from PySide2.QtSvg import *
from PySide2.QtGui import *

# from DetermineBoundsRevised import determine_bounds


def xy_to_angles(x,y, motor_1_pos=-1.5, motor_2_pos=1.5, driver=3.34, follower=4.82):

    L1 = driver
    L2 = follower
    a = 1.5

    x = float(x)
    y = float(y)   

    L3 = sqrt( (x+a)**2 + y**2)
    L4 = sqrt( (x-a)**2 + y**2)

    pi = 3.141592653589793

    # NOTE: output of the acos function is in radians, so we multiply by 180/pi to convert to degrees
    theta_3 = acos(  (  (L3**2) + (2*a)**2 - L4**2  )  /  (2*L3*2*a)  ) * 180/pi
    theta_4 = acos(  (  (L4**2) + (2*a)**2 - L3**2  )  /  (2*L4*2*a)  ) * 180/pi
    theta_5 = acos(  ( L1**2 + L3**2 - L2**2  ) / (2*L1*L3)  ) * 180/pi
    theta_6 = acos(  ( L1**2 + L4**2 - L2**2  ) / (2*L1*L4)  ) * 180/pi

    theta_1 = 180 - theta_5 - theta_3
    theta_2 = 180 - theta_4 - theta_6

    # The motors are positioned forward, with zero being the forward position, 
    # 90 being rotated anti-clockwise 90 degrees, and -90 being rotated 
    # clockwise by 90 degrees
    left_motor_angle = 90 - theta_1
    right_motor_angle = theta_2 - 90

    return (left_motor_angle, right_motor_angle)


def SketchAndVisualize(image_path):
    import os
    path = os.path.abspath(linedraw.__file__)
    # print("PATH:")
    # print(path)
    lines = linedraw.sketch(image_path)
    SVG_to_image(input_folder="../gui/output/")
    

    lines = scale_image(lines)

    for i, line in enumerate(lines):
      for j, point in enumerate(line):
        lines[i][j] = xy_to_angles(point[0],point[1])

    # Rename to something more appropriate, now that we have angles instead of lines
    angles = lines

    SendDataToPi.send_angles_and_begin_drawing(angles)
    
    
    print("DONE!")


def SVG_to_image(input_folder="../gui/output/"):

  svgFilepath = input_folder + "out.svg"
  pngFilepath = input_folder + "out.png"
  resolution = 2560

  # Perform conversion
  r=QSvgRenderer(svgFilepath)
  height=r.defaultSize().height()*resolution/r.defaultSize().width()
  i=QImage(resolution,height,QImage.Format_ARGB32)
  p=QPainter(i)
  r.render(p)
  i.save(pngFilepath)
  p.end()