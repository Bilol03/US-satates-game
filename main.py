import turtle
import pandas as pd
screen  = turtle.Screen()

screen.title("US States Game")
img = 'blank_states_img.gif'
screen.screensize(canvwidth=400, canvheight=400)
screen.addshape(img)
turtle.shape(img)

states = pd.read_csv('50_states.csv')
all_states = states.state.to_list()
print(len(states))


len_res = []
game_is_on = True
while game_is_on:
    user_answer = screen.textinput(title=f"{len(len_res)}/50, Guess the state name", prompt="What is the state name that you choose? ")
    if user_answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == user_answer]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(arg=user_answer, font=('Arial', 12, 'normal'))

        if user_answer not in len_res:
            len_res.append(user_answer)
    print(len_res)
    if len(len_res) == len(states):
        game_is_on = False

screen.exitonclick()