# I was inspired by https://www.youtube.com/watch?v=ogsRn1XSy5c in writing this program.

# Below I have provided explanation about the methods used in this program

# 1. import turtle: To use the graphics created by the turtle graphics we need to import the module.

# 2. turtle.bgcolor('black'): Turns the background color of our window to black.

# 3. myTurtle = turtle.Turtle(): Creates a turtle object called myTurtle. Think of myTurtle as an actual pet turtle
# which understands English and can understand you when you tell it to move left, right, etc.

# 4. myTurtle.pencolor("red"): When you pet turtle is moving it leaves a red trace behind creating beautiful graphics.

# 5. myTurtle.speed(30): Tells your pet turtle how fast it should move.

# 6. myTurtle.forward(number + 1): Tells your pet turtle to move forward by number+1 (gets incremented by one in each
# iteration of the loop).

# 7. myTurtle.right(89): Tells your pet turtle to turn right by 89 degrees.

import turtle

turtle.bgcolor('black')
myTurtle = turtle.Turtle()
myTurtle.pencolor("red")
myTurtle.speed(30)

for number in range(300):
    myTurtle.forward(number + 1)
    myTurtle.right(89)

turtle.mainloop()




