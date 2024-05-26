# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle()

# Step 3: Move in the direction Bob's facing for 50 pixels
bob.forward(50)

# Step 4: We're done!
turtle.done()

##################################
silly = turtle.Turtle()

silly.forward(50)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

turtle.done()

###################################
smart = turtle.Turtle()

# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(4):
    smart.forward(50)
    smart.right(90)
    
# This isn't indented, so we aren't repeating it.
turtle.done()

#####################################

print("start test")

for i in range(4):
    print(i)
    print("test")
    
print("end test 1")

for banana in range(20):
    print(banana)
    print(banana * 2)
    
########################################

star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(144)
    
turtle.done()
#########################################

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()

#################################

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()

#############################

import turtle 

painter2 = turtle.Turtle()

painter2.pencolor("#32D486")
painter2.forward(30)

painter2.pencolor("#D6305F")
painter2.forward(30)

######################################

import turtle 

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()

########################################

seurat = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)
    
turtle.done()

###############################################

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
