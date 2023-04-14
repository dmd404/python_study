from turtle import Screen


def main():
    screen = Screen()
    screen.title('My pong game')
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.exitonclick()


if __name__ == '__main__':
    main()
