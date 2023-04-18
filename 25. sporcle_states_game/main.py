import turtle
import pandas as pd


screen = turtle.Screen()
screen.title('U.S. States Game')
player = turtle.Turtle()

def get_mouse_click_cor(x, y):
    print(x, y)


def main():
    image = 'blank_states_img.gif'
    screen.addshape(image)
    turtle.goto(20, 0)
    turtle.shape(image)
    guess_cnt = 1

    state_df = pd.read_csv('50_states.csv')
    state_list = state_df['state'].str.lower().to_list()
    state_ser = state_df.state.str.lower()
    answer = 'iowa'

    # state = state_df[state_df.state == 'Iowa']
    # print(int(state.x))
    # print(state)
    for name in state_list:
        answer_state = screen.textinput(title=f'{guess_cnt}/50 Guess the state'.title(),
                                        prompt="What's another state's name?").lower()

        state = state_df[state_ser == answer_state]
        if answer_state in state_list:
            guess_cnt += 1
            state_x = int(state.x)
            state_y = int(state.y)
            player.hideturtle()
            player.penup()
            player.goto(state_x, state_y)
            player.write(answer_state)
        else:
            pass
    print(f'Your score is {guess_cnt} out of 50.')

        # if answer_state in state_list:
        #     guess_cnt += 1
        #     turtle.goto(state_x, state_y)
        #     turtle.write(answer_state)
        # else:
        #     pass

        # print(f'Your score is {guess_cnt}')
    # check if guess is among the 50 states

if __name__ == '__main__':
    main()
