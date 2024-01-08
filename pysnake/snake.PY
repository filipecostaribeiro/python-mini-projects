import curses
import time

def game_loop(window):
    #print a str
    for n in range(1,5):
        window.addstr(f"Aperte alguma tecla:\n")
        window.refresh()
        time.sleep(0.5)
    """
    while True:
        window.addstr(f"O valor de i é {i}\n")
        window.refresh()
        time.sleep(0.5)
    """

curses.wrapper(game_loop)