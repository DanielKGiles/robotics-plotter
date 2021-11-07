import pickle
import numpy as np
from ImplementingLinedraw import xy_to_angles


#######################################################
# This section creates the rectangle with very few points

bottom_left_coordinate = (-1.87,4.25)
bottom_right_coordinate = (1.87,4.25)
top_right_coordinate = (1.87,7.05)
top_left_coordinate = (-1.87,7.05)


lines = [[bottom_left_coordinate, bottom_right_coordinate, top_right_coordinate, top_left_coordinate, bottom_left_coordinate]]

for i, line in enumerate(lines):
   for j, point in enumerate(line):
      lines[i][j] = xy_to_angles(point[0],point[1])

print(lines)

with open('rectangle.pkl', 'wb') as f:
   pickle.dump(lines, f)

## Plot the rectangle 
# import matplotlib.pyplot as plt
# x_list = []
# y_list = []
# for x,y in points:
#    x_list.append(x)
#    y_list.append(y)

# plt.plot(x_list,y_list)
# plt.show()


###########################################################
# The same rectangle with more points can be created below


bottom_line_x_values = []
step = 0.17
for x in np.arange(-1.87, 1.87+step, step):
   bottom_line_x_values.append(x)
bottom_line_y_values = [4.25]*len(bottom_line_x_values)

bottom_line = []
for i in range(len(bottom_line_x_values)):
   x = bottom_line_x_values[i]
   y = bottom_line_y_values[i]
   bottom_line.append((x,y))

#_____________________________________________________________

right_line_y_values = []
step = 0.2
for y in np.arange(4.25, 7.05+step, step):
   right_line_y_values.append(y)
right_line_x_values = [1.87]*len(right_line_y_values)

right_line = []
for i in range(len(right_line_x_values)):
   x = right_line_x_values[i]
   y = right_line_y_values[i]
   right_line.append((x,y))

#_____________________________________________________________


top_line_x_values = []
step = 0.17
for x in np.arange(-1.87, 1.87+step, step):
   top_line_x_values.append(x)
top_line_y_values = [7.05]*len(top_line_x_values)

top_line = []
for i in range(len(top_line_x_values)):
   x = top_line_x_values[i]
   y = top_line_y_values[i]
   top_line.append((x,y))

#_____________________________________________________________


left_line_y_values = []
step = 0.2
for y in np.arange(4.25, 7.05+step, 0.2+step):
   left_line_y_values.append(y)
left_line_x_values = [-1.87]*len(left_line_y_values)

left_line = []
for i in range(len(left_line_x_values)):
   x = left_line_x_values[i]
   y = left_line_y_values[i]
   left_line.append((x,y))


lines = [bottom_line, right_line, top_line, left_line]

# ____________________________________________________
# Convert to angles and save data

count = 0
for i, line in enumerate(lines):
   for j, point in enumerate(line):
      count += 1
      lines[i][j] = xy_to_angles(point[0],point[1])

print(lines)

with open('detailed_rectangle.pkl', 'wb') as f:
   pickle.dump(lines, f)

# _______________________________________
# Plot

# import matplotlib.pyplot as plt

# plt.plot(bottom_line_x_values,bottom_line_y_values, color='lime')
# plt.plot(right_line_x_values,right_line_y_values, color='blue')
# plt.plot(top_line_x_values,top_line_y_values, color='red')
# plt.plot(left_line_x_values,left_line_y_values, color='black')
# plt.show()

print("Done saving rectangles")