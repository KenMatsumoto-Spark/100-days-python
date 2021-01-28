
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)

states_data = pandas.read_csv("50_states.csv")

right_guesses = 0
user_answers = []
is_game_on = True

def is_state_in_states_data(answer_state, states_data):
    if answer_state == "Exit":
        global is_game_on
        is_game_on = False
        missing_states = []
        for state in states_data.state.to_list():
            if state not in user_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        return
    for state in states_data.state.tolist():
        if answer_state == state:
            if answer_state in user_answers:
                return
            user_answers.append(answer_state)
            global right_guesses
            right_guesses += 1
            x_cor = int(states_data[states_data.state == answer_state].x)
            y_cor = int(states_data[states_data.state == answer_state].y)
            text = turtle.Turtle()
            text.hideturtle()
            text.penup()
            text.color("black")
            text.goto(x_cor, y_cor)
            text.write(answer_state)




while is_game_on:
    screen.update()
    answer_state = screen.textinput(title=f"{right_guesses}/50 States Correct", prompt="What's another state's name?").title()
    is_state_in_states_data(answer_state, states_data)

