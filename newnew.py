from turtle import Turtle,Screen
from random import choice
window=Screen()
def winner(turtle):
    window.bgcolor('gray')
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pencolor('white')
    turtle.write('You Win.....',font=('arial',20,'bold'),align='center')
def loser(turtle):
     window.bgcolor('black')
     turtle.hideturtle()
     turtle.penup()
     turtle.goto(0,0)
     turtle.pencolor('white')
     turtle.write('You lose.....',font=('arial',20,'bold'),align='center')
window.title('Turtle Race')
window.bgcolor('black')
window.setup(800,800)
first_turtle=Turtle()
second_turtle=Turtle()
third_turtle=Turtle()
first_turtle.color('blue')
second_turtle.color('red')
third_turtle.color('yellow')
first_turtle.shape('turtle')
first_turtle.shapesize(1.5)
second_turtle.shape('turtle')
second_turtle.shapesize(1.5)
third_turtle.shape('turtle')
third_turtle.shapesize(1.5)
first_turtle.penup()
second_turtle.penup()
third_turtle.penup()
first_turtle.goto(-380,0)
second_turtle.goto(-380,200)
third_turtle.goto(-380,-200)
turtles=[first_turtle,second_turtle,third_turtle]
winner_turtle=0
color=0
user_choice=window.textinput(title='Make your bet',prompt='Tybe a color : Red,Blue or yellow ?').lower()

while first_turtle.xcor()<380 and second_turtle.xcor()<380 and third_turtle.xcor()<380:
    first_turtle.forward(choice(range(20,60)))
    second_turtle.forward(choice(range(20,60)))
    third_turtle.forward(choice(range(20,60))) 
for i in turtles:
  if i.xcor()>380:
       winner_turtle=i
       color=i.color()
if color[1]==user_choice:
    winner(winner_turtle)
else:
    loser(winner_turtle)
window.exitonclick()