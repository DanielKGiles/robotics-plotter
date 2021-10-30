from math import *
import turtle


def xy_to_angles(x,y):

   x = float(x)
   y = float(y)

   L1 = 0.1
   L2 = 100
   a = 1.5

   L3 = sqrt( (x+a)**2 + y**2)
   L4 = sqrt( (x-a)**2 + y**2)

   try:
      theta_3 = acos(  (  (L3**2) + (2*a)**2 - L4**2  )  /  (2*L3*2*a)  )
   except:
      print("THETA_3 ERROR")
      print(x, y)
      print((L3**2) + (2*a)**2 - L4**2 , (2*L3*2*a))
   
   try:
      theta_4 = acos(  (  (L4**2) + (2*a)**2 - L3**2  )  /  (2*L4*2*a)  )
   except:
      print("THETA_4 ERROR")
      print(x, y)
      print((L4**2) + (2*a)**2 - L3**2, (2*L4*2*a))
   
   try:
      theta_5 = acos(  ( L1**2 + L3**2 - L2**2  ) / (2*L1*L3)  )
   except:
      print("THETA_5 ERROR")
      print(x, y)
      print(L1**2 + L3**2 - L2**2, 2*L1*L3)

   try:
      theta_6 = acos(  ( L1**2 + L4**2 - L2**2  ) / (2*L1*L4)  )
   except:
      print("THETA_6 ERROR")
      print(x, y)
      print(L1**2 + L4**2 - L2**2, 2*L1*L4)

   theta_1 = 180 - theta_5 - theta_3
   theta_2 = 180 - theta_4 - theta_6


def generate_angles(lines):
   angles = []
   for i in range(len(lines)):
      line = lines[i]
      angles.append([]) # Add space for a new line
      for j in range(len(line)):
         (x,y) = line[j]
         angles[i].append(xy_to_angles(x,y))


def set_bounds(lines):
      
   # First, we create a pair of empty sets for all the x and y values in all of the lines of the plot data.
   x_values_in_lines = set()
   y_values_in_lines = set()

   # Loop over each line and all the points in each line, to get sets of all the x and y values:
   for line in lines:

      x_values_in_line, y_values_in_line = zip(*line)

      x_values_in_lines.update(x_values_in_line)
      y_values_in_lines.update(y_values_in_line)

   # Identify the minimum and maximum values.
   min_x, max_x = min(x_values_in_lines), max(x_values_in_lines)
   min_y, max_y = min(y_values_in_lines), max(y_values_in_lines)

   print("Range in x: " + str(min_x), str(max_x))
   print("Range in y: " + str(min_y), str(max_y))

   

