import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "./Day_25/US states game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get cor of states
# def get_mouse_click_cor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
data = pandas.read_csv("./Day_25/US states game/50_states.csv")
states_list = data.state.to_list()
guessed_states = []

# User to keep guessing
while len(guessed_states) < 6: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states_list)} Guess the state", prompt="What's anothe state name?").title()

    # If answer is one of the states in all the states of the 50_states.csv
    if answer_state in states_list:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
    if answer_state == "Exit":
        # LIst comprehension
        missing_states = [state for state in states_list if state not in guessed_states]
        missed_data = pandas.DataFrame(missing_states)
        missed_data.to_csv("./Day_25/US states game/states_to_learn.csv")
        break

