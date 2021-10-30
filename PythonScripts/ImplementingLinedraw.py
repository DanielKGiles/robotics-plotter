import cv2
import linedraw
import sys
sys.path.append('../PythonScripts/')
import plotter
import pickle
import SendDataToPi

def SketchAndVisualize(image_path):
    lines = linedraw.sketch(image_path)
    # print(lines)
    # file = open("./output/lines.txt", "a")
    # file.write(lines)
    # file.close()


    # linedraw.visualize(lines) 


    # line_plotter = plotter.pantograph_plotter()
    # angles = line_plotter.generate_angles(lines)

    
    # angles = plotter2.generate_angles(lines)
    # print(angles)
    
    # plotter.set_bounds(lines)

    SendDataToPi.send_lines_and_begin_drawing(lines)
    
    print("DONE!")
