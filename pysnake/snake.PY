import curses
import time

def game_loop(window):
    while True:
        window.addstr(f"O valor de i é {i}\n")
        window.refresh()
        time.sleep(0.5)

curses.wrapper(game_loop)