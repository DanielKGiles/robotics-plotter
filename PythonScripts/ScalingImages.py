def scale_image(lines, left_bound=-3.5, right_bound=3.5, bottom_bound=2, top_bound=5.5):
   current_min_x = 10000
   current_min_y = 10000
   current_max_x = -10000
   current_max_y = -10000
   for i, line in enumerate(lines):
      for j, point in enumerate(line):
         if current_min_x > point[0]:
            current_min_x = point[0]
         if current_max_x < point[0]:
            current_max_x = point[0]
         if current_min_y > point[1]:
            current_min_y = point[1]
         if current_max_y < point[1]:
            current_max_y = point[1]


   print("current_min_x = ",current_min_x)
   print("current_max_x = ",current_max_x)
   print("current_min_y = ",current_min_y)
   print("current_max_y = ",current_max_y)

   current_x_range = current_max_x - current_min_x
   current_y_range = current_max_y - current_min_y

   desired_x_range = right_bound - left_bound
   desired_y_range = top_bound - bottom_bound


   # Center points around the origin
   for i, line in enumerate(lines):
      for j, point in enumerate(line):
         x = lines[i][j][0] - ( (current_min_x + current_max_x) / 2 )
         y = lines[i][j][1] - ( (current_min_y + current_max_y) / 2 )

         lines[i][j] = (x,y)

   # Scale the points
   scaling_factor = max(current_max_x - current_min_x, current_max_y - current_min_y) / (top_bound - bottom_bound)
   for i, line in enumerate(lines):
      for j, point in enumerate(line):
         x = lines[i][j][0] / scaling_factor
         y = lines[i][j][1] / scaling_factor

         lines[i][j] = (x,y)

   # Translate points to the correct position
   for i, line in enumerate(lines):
      for j, point in enumerate(line):
         x = lines[i][j][0]
         y = lines[i][j][1] + (bottom_bound + top_bound) / 2

         lines[i][j] = (x,y)

   return lines


