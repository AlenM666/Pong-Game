import turtle

#create screen
sc = turtle.Screen()
sc.title("Pong-Game")
sc.bgcolor("black")
sc.setup(width=1000, height=1000)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)




while True:
    sc.update()
    continue

