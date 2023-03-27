import turtle
# import winsound

wn = turtle.Screen()  # creat a window
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)  # make our prog faster


# score
score_A = 0
score_B = 0

# paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape('square')
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.color('white')
paddle_A.penup()
paddle_A.goto(-350, 0)  # pos


# paddle-B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape('square')
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.color('white')
paddle_B.penup()
paddle_B.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write('Player A: {}   Player B: {}'.format(score_A, score_B), align='center', font=('Times New Roman', 20, 'italic'))

# function
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

# keybord binding
wn.listen()
wn.onkeypress(paddle_A_up, 'z')
wn.onkeypress(paddle_A_down, 's')
wn.onkeypress(paddle_B_up, 'Up')
wn.onkeypress(paddle_B_down, 'Down')


# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #   winsound.PlaySound("light", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_A, score_B), align='center', font=('Times New Roman', 20, 'italic'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_A, score_B), align='center', font=('Times New Roman', 20, 'italic'))

    # paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_B.ycor() + 45 and ball.ycor() > paddle_B.ycor() - 45):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_A.ycor() + 45 and ball.ycor() > paddle_A.ycor() - 45):
        ball.setx(-340)
        ball.dx *= -1


