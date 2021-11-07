import numpy as np
from math import *
import matplotlib.pyplot as plt
import pickle

import sys
sys.path.append('../PythonScripts/')
sys.path.append('../gui/')
from ScalingImages import scale_image

def hypotenuse(side1, side2):
    return sqrt(side1 ** 2 + side2 ** 2)

# def xy_to_angles(x=0, y=None, motor_1_pos=-1.5, motor_2_pos=1.5, driver=3.34, follower=4.82):

#    # if y is None:
#    #    y = self.furthest_reach

#    # Given a pair of x/y co-ordinates, returns the angle required of each arm.

#    # we add L to y, so that y=0 is a safe distance from the motors

#    # y = y + self.adder

#    # calculate the x value relative to each motor
#    x_relative_to_motor_1 = motor_1_pos - x
#    x_relative_to_motor_2 = motor_2_pos - x

#    # calculate the distance from each motor to the x/y point
#    d1 = hypotenuse(x_relative_to_motor_1, y)
#    d2 = hypotenuse(x_relative_to_motor_2, y)

#    # # calculate the angle between the d line and arm
#    # inner_angle_1 = acos((d1/self.L)/2)
#    # inner_angle_2 = acos((d2/self.L)/2)

#    # calculate the angle between the d line and driver arm
#    inner_angle_1 = acos((driver **2 + d1 ** 2 - follower ** 2) / (2 * driver * d1))
#    inner_angle_2 = acos((driver **2 + d2 ** 2 - follower ** 2) / (2 * driver * d2))

#    # calculate the angle between the d line and the vertical
#    outer_angle_1 = - atan(x_relative_to_motor_1/y)
#    outer_angle_2 = - atan(x_relative_to_motor_2/y)

#    # calculate the sum of the angles in degrees
#    angle1 = degrees(outer_angle_1 - inner_angle_1)
#    angle2 = degrees(inner_angle_2 + outer_angle_2)

#    return (
#       angle1 * self.angle_multiplier,
#       angle2 * self.angle_multiplier
#       )


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

   # print("THETA 1: " + str(theta_1))
   # print("THETA 2: " + str(theta_2))

   # # The motors are positioned forward, with zero being the forward position, 
   # # 90 being rotated anti-clockwise 90 degrees, and -90 being rotated 
   # # clockwise by 90 degrees
   # left_motor_angle = 90 - theta_1
   # # right_motor_angle = -1*theta_2
   # right_motor_angle = theta_2 - 90

   # return (left_motor_angle, right_motor_angle)

   if (theta_1 < 0):
      raise Exception
   elif (theta_2 < 0):
      raise Exception

   return (theta_1, theta_2)




def determine_bounds(driver=3.34, follower=4.82, lines=None):

   if lines == None:
      with open(r'C:\Users\danie\Documents\Academics\CurrentClasses\Fall 2021\Robotics\robotics_plotter_repo\robotics-plotter\gui\lines.pkl', 'rb') as f:
         lines = pickle.load(f)

   acceptable_points = []
   acceptable_angles = []
   acceptable_x = []
   acceptable_y = []
   # first_error = True
   for x in np.arange(-10,10,0.01):
      for y in np.arange(0,10,0.01):
         # acceptable_points.append(xy_to_angles(x,y))
         try:
            # acceptable_points.append((x,y))
            acceptable_angles.append(xy_to_angles(x,y))
            acceptable_points.append((x,y))
            acceptable_x.append(x)
            acceptable_y.append(y)

         except Exception as e:
            # if first_error:
            #    first_error = False
            #    print(e)
            ...

   # Set the min and max values to number that we know will be changed below
   min_x = 1000
   min_y = 1000

   max_x = -1000
   max_y = -1000
   for i in range(len(acceptable_points)):
      x = acceptable_points[i][0]
      y = acceptable_points[i][1]

      if x < min_x:
         min_x = x
      if x > max_x:
         max_x = x
      if y < min_y:
         min_y = y
      if y > max_y:
         max_y = y
      
   # print("min_x, min_y = ", min_x, ", ", min_y)
   # print("max_x, max_y = ", max_x, ", ", max_y)

   plt.plot(acceptable_x, acceptable_y)

   x_min_less_than_73 = 10
   x_max_less_than_73 = 0
   for i in range(len(acceptable_points)):
      if ((acceptable_points[i][1] > 7.3) and (acceptable_points[i][0] < x_min_less_than_73)):
         x_min_less_than_73 = acceptable_points[i][0]
      if ((acceptable_points[i][1] > 7.3) and (acceptable_points[i][0] > x_max_less_than_73)):
         x_max_less_than_73 = acceptable_points[i][0]
   # print("x_min_less_than_6", x_min_less_than_6)
   # print("x_max_less_than_6", x_max_less_than_6)
   x_range = [x_min_less_than_73, x_min_less_than_73, x_max_less_than_73, x_max_less_than_73, x_min_less_than_73]
   y_range = [4,7.3,7.3,4, 4]
   plt.plot(x_range,y_range, color='red')

   offset = 0.25

   new_x_range = [x_min_less_than_73 + offset, x_min_less_than_73 + offset, x_max_less_than_73 - offset, x_max_less_than_73 - offset, x_min_less_than_73 + offset]
   new_y_range = [y_range[0] + offset, y_range[1] - offset, y_range[1] - offset, y_range[0] + offset, y_range[0] + offset]
   plt.plot(new_x_range,new_y_range, color='lime')

   x_bounds = [x_min_less_than_73 + offset, x_max_less_than_73 - offset]
   y_bounds = [y_range[0] + offset, y_range[1] - offset]

   print("X-bounds --> Left: " + str(x_bounds[0]) + ", Right: " + str(x_bounds[1]))
   print("Y-bounds --> Bottom: " + str(y_bounds[0]) + ", Top: " + str(y_bounds[1]))

   lines = scale_image(lines, left_bound=x_bounds[0], right_bound=x_bounds[1], bottom_bound=y_bounds[0], top_bound=y_bounds[1])
   # separate the x and y for easy plotting.
   x = []
   y = []
   for i, line in enumerate(lines):
      for j, point in enumerate(line):
         x.append(lines[i][j][0])
         y.append(lines[i][j][1])
   plt.plot(x,y,'pink')

   plt.show()







   # print(acceptable_points)
   # print(acceptable_angles)

determine_bounds()