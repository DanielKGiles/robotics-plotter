import pickle
from ImplementingLinedraw import xy_to_angles

lines = [[(0,3),(0,3)]] # This is the point where the robot should go so that erasing can be done

for i, line in enumerate(lines):
   for j, point in enumerate(line):
      lines[i][j] = xy_to_angles(point[0],point[1])

print(lines)

with open('erase.pkl', 'wb') as f:
   pickle.dump(lines, f)

   