import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snakey Game")
screen.tracer(0)

snakey = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")
screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snakey.move()

    if snakey.head.distance(food) < 20:
        food.refresh()
        snakey.extend()
        scoreboard.increase_score()

    if snakey.head.xcor() > 280 or snakey.head.xcor() < -280 or snakey.head.ycor() > 280 or snakey.head.ycor() < -280:
        scoreboard.reset()
        snakey.reset()

    for segment in snakey.body[1:]:
        if snakey.head.distance(segment) < 10:
            scoreboard.reset()
            snakey.reset()


screen.exitonclick()
