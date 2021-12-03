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



while True:
    sc.update()
    continue

