#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner ==2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner ==3:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner ==4:
        alice.right(90)
        alice.forward(50)
        alice.left(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
def squaresInSquares(t, num):
    size = 200  # Initial size of the outermost square

    for i in range(num):
        for _ in range(4):  # Draw a square
            t.forward(size)
            t.right(90)
        size -= 20  # Reduce the size for the next square
        t.penup()
        t.forward(10)  # Move turtle to the starting point of the next smaller square
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()
        
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 4)
    #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
