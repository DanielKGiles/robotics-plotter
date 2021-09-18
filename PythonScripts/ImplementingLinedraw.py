import cv2
import linedraw

def SketchAndVisualize(image_path):
    lines = linedraw.sketch(image_path)
    linedraw.visualize(lines) 