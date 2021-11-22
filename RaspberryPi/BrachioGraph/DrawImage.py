# import pantograph
import pickle
import turtle
from pantograph import *

pickle_file = open("lines.pkl","rb")

objects = []

while True:
    try:
        objects.append(pickle.load(pickle_file))
    except EOFError:
        break

pickle_file.close()

lines = objects[0]

# print(lines)
print("LINES EXTRACTED FROM PICKLE FILE")

pg = PantoGraph(driver=5, follower=10, motor_1_pos=-1.5, motor_2_pos=1.5)

pg.set_angles(0,0)
pg.set_angles(-15,0)
pg.set_angles(0,15)
pg.set_angles(-15,15)
pg.set_angles(-16,16)
pg.set_angles(-17,17)
pg.set_angles(-18,18)
pg.set_angles(-18,18)
pg.set_angles(-19,19)
pg.set_angles(-20,20)
pg.set_angles(-21,21)
pg.set_angles(-22,22)
pg.set_angles(-23,23)
pg.set_angles(-24,24)
pg.set_angles(-25,25)
# pg.set_angles(-89,89)
pg.set_angles(0,0)

print("ANGLES WERE SET!")

pg.plot_lines(lines=lines, bounds=[-1,6,1,7])
print("LINES HAVE BEEN PLOTTED!")


def draw_with_turtle(lines):
    turtle.speed(0) # Fastest
    for line in lines:
        turtle.penup()
        x = line[0][0]*640/1024-320
        y = line[0][1]*640/1024-320
        turtle.goto(x, y)
        turtle.pendown()
        for x,y in line:
            x = x*640/1024-320
            y = y*640/1024-320
            turtle.goto(x,y)
            # print("(" + str(x) + "," + str(y))

draw_with_turtle(lines)


