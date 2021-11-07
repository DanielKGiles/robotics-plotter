import pickle
from ImplementingLinedraw import xy_to_angles

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

# import matplotlib.pyplot as plt
# x_list = []
# y_list = []
# for x,y in points:
#    x_list.append(x)
#    y_list.append(y)

# plt.plot(x_list,y_list)
# plt.show()
