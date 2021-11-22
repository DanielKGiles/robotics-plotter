import turtle

def DrawWithTurtle(lines):
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