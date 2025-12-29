import turtle
import pandas



writer = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us_states_map.gif"
screen.addshape(image)
turtle.shape(image)


num_correct_gues = 0
correct_guesses = []




data = pandas.read_csv("us_states_coordinates.csv")
data_state = data["state"].to_list()
print(data_state)

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title = f"{num_correct_gues}/50 States Correct",
                                    prompt= "what's another states name?").title()
    if answer_state == "Exit":
        break
    if answer_state in data_state and answer_state not in correct_guesses:
        print(answer_state)
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == answer_state]
        x_coor = int(state_data.x)
        y_coor = int(state_data.y)
        writer.goto(x_coor, y_coor)
        writer.write(answer_state, align="center", font=("Arial", 9, "normal"))
        correct_guesses.append(answer_state)
        num_correct_gues += 1

state_to_learn = [element for element
                  in data_state if element not in correct_guesses]

learn_data = pandas.DataFrame(state_to_learn)
learn_data.to_csv("states_to_learn.csv")







# screen.exitonclick()