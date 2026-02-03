import turtle
import pandas
from show_name import Name

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
name = Name()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct = 0
input_title = "Guess the state"
correct_guesses =[]
while len(correct_guesses) < 50:
        answer_state = screen.textinput(title=input_title, prompt="What's another state's name?").title()
        # if answer_state in data["state"].values and answer_state != correct_guesses:
        if answer_state == "Exit":
            df = pandas.DataFrame(all_states)
            df.to_csv("states_to_learn.csv")

        if answer_state in all_states:
            all_states.remove(answer_state)
            correct += 1
            correct_guesses.append(answer_state)
            state = data[data.state == answer_state]
            x_cor = int(state.x.iloc[0])
            y_cor = int(state.y.iloc[0])
            coordinates = (x_cor,y_cor)
            name.print(answer_state,coordinates)
            input_title = f"{correct}/50 correct"

screen.exitonclick()