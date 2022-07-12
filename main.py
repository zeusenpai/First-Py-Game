import turtle
import winsound

def play(user_a, user_b):
    window = turtle.Screen()
    window.title('Pong!')
    window.bgcolor('black')
    window.setup(width=800, height=600)
    window.tracer(0)

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape('square')
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape('square')
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('square')
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

    # Head
    head = turtle.Turtle()
    head.speed(0)
    head.color("white")
    head.penup()
    head.hideturtle()
    head.goto(0, 260)
    head.write("Pong!", align="center", font=("Courier", 24, "bold"))

    #  Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 230)
    pen.write("{}: 0 | {}: 0".format(user_a, user_b), align='center', font=('Courier', 16, "normal"))


    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # Key Bindings
    window.listen()
    window.onkeypress(paddle_a_up, "w")
    window.onkeypress(paddle_a_down, "s")
    window.onkeypress(paddle_b_up, "Up")
    window.onkeypress(paddle_b_down, "Down")

    # Main Game Loop

    # Score
    score_a = 0
    score_b = 0

    while True:
        window.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 220:
            ball.sety(220)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if paddle_a.ycor() > 190:
            paddle_a.sety(190)

        if paddle_a.ycor() < -250:
            paddle_a.sety(-250)

        if paddle_b.ycor() > 190:
            paddle_b.sety(190)

        if paddle_b.ycor() < -250:
            paddle_b.sety(-250)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("{}: {} | {}: {}".format(user_a, score_a, user_b, score_b), align='center', font=('Courier', 16, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("{}: {} | {}: {}".format(user_a, score_a, user_b, score_b), align='center',
                      font=('Courier', 16, "normal"))

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)







