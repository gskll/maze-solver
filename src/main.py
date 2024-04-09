from window import Window


def main():
    screen_x = 800
    screen_y = 600

    win = Window(screen_y, screen_x)
    win.wait_for_close()


main()
