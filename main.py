import turtle

#create screen
sc = turtle.Screen()
sc.title("Pong-Game")
sc.bgcolor("black")
sc.setup(width=1500, height=1500)

# Left paddle
left_board = turtle.Turtle()
left_board.speed(0)
left_board.shape("square")
left_board.color("white")
left_board.shapesize(stretch_wid=6, stretch_len=2)
left_board.penup()
left_board.goto(-600,0)


#right paddle
right_board = turtle.Turtle()
right_board.speed(0)
right_board.shape("square")
right_board.color("white")
right_board.shapesize(stretch_wid=6, stretch_len=2)
right_board.penup()
right_board.goto(600,0)


#ball in shape of a circle
bounce_ball = turtle.Turtle()
bounce_ball.speed(60)
bounce_ball.shape("circle")
bounce_ball.color("white")
bounce_ball.penup()
bounce_ball.goto(0, 0)
bounce_ball.dx = 7
bounce_ball.dy = -7


#score
right_player = 0
left_player = 0

#score display
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.goto(0, 460)
sketch.write("Left player : 0    Right player : 0", align="center", font=("Courier", 24,"normal"))

#move player vertacly
def boardleaup():
    y = left_board.ycor()
    y += 40
    left_board.sety(y)
def boardleadown():
    y = left_board.ycor()
    y -= 40
    left_board.sety(y)
def boardlebup():
    y = right_board.ycor()
    y += 40
    right_board.sety(y)
def boardlebdown():
    y = left_board.ycor()
    y -= 40
    left_board.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(boardleaup, "e")
sc.onkeypress(boardleadown, "x")
sc.onkeypress(boardlebup, "Up")
sc.onkeypress(boardlebdown, "Down")


while True:
    sc.update()

    bounce_ball.setx(bounce_ball.xcor()*bounce_ball.dx)
    bounce_ball.setx(bounce_ball.xcor()*bounce_ball.dy)

    #checking borders
    if bounce_ball.ycor() > 280:
        bounce_ball.sety(280)
        bounce_ball.dy *= -1

    if bounce_ball.ycor() < -280:
        bounce_ball.sety(-280)
        bounce_ball.dy *= -1


    if bounce_ball.xcor() > 500:
        bounce_ball.goto(0, 0)
        bounce_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    continue




















