#In this game, the player moves the turtle around the screen using the arrow keys to catch the food item, which moves randomly around the screen. 
#Each time the player catches the food, their score increases by 10, and the food moves to a new random location. 
#The score is displayed at the top of the screen using a turtle object that writes the current score to the screen.
import turtle
import random

# set up the window
window = turtle.Screen()
window.title("Turtle Catch Game")
window.bgcolor("light blue")
window.setup(width=500, height=500)

# create the turtle player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# create the food turtle
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-200, 200), random.randint(-200, 200))

# set up the score
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-200, 230)
score_turtle.write(f"Score: {score}", font=("Arial", 16, "normal"))

# set up the game loop
def move_up():
    player.setheading(90)
    player.forward(10)

def move_down():
    player.setheading(270)
    player.forward(10)

def move_left():
    player.setheading(180)
    player.forward(10)

def move_right():
    player.setheading(0)
    player.forward(10)

window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

while True:
    # move the food
    food.forward(10)
    
    # check if the food is off the screen
    if food.xcor() < -250 or food.xcor() > 250 or food.ycor() < -250 or food.ycor() > 250:
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
    
    # check if the player has caught the food
    if player.distance(food) < 20:
        score += 10
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", font=("Arial", 16, "normal"))
        food.goto(random.randint(-200, 200), random.randint(-200, 200))

window.mainloop()
