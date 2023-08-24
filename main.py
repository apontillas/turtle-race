from turtle import Turtle, Screen
import random
from score import Score

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
is_race_on = False
y = -100
score = Score()


for turtle_i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 40
    all_turtles.append(new_turtle)
    print(all_turtles)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                score.winner()
                print(f'You won! The winning color is {winning_color}')
            else:
                score.loser()
                print(f'You have lost! The {winning_color} turtle is the winner!')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
