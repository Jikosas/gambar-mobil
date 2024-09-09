import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Gambar Mobil")

# Create a turtle object
mobil = turtle.Turtle()

# Draw the body of the car
mobil.penup()
mobil.goto(-100, -50)
mobil.pendown()
mobil.color("blue")
mobil.begin_fill()
mobil.forward(200)
mobil.left(90)
mobil.forward(50)
mobil.left(90)
mobil.forward(200)
mobil.left(90)
mobil.forward(50)
mobil.end_fill()

# Draw the roof of the car
mobil.penup()
mobil.goto(-60, 0)
mobil.pendown()
mobil.color("blue")
mobil.begin_fill()
mobil.left(90)
mobil.forward(120)
mobil.left(45)
mobil.forward(70)
mobil.left(45)
mobil.forward(120)
mobil.left(45)
mobil.forward(70)
mobil.end_fill()

# Draw the wheels of the car
mobil.penup()
mobil.goto(-75, -50)
mobil.pendown()
mobil.color("black")
mobil.begin_fill()
mobil.circle(20)
mobil.end_fill()

mobil.penup()
mobil.goto(75, -50)
mobil.pendown()
mobil.color("black")
mobil.begin_fill()
mobil.circle(20)
mobil.end_fill()

# Hide the turtle and display the window
mobil.hideturtle()
turtle.done()
