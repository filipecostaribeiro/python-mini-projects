import curses

def game_loop(window):
    # Sets the cursor visibility to invisible.
    curses.curs_set(0)
    # Draw a border around a window with a default border style.
    window.border(0)
    height = window.getmaxyx()[0]
    width = window.getmaxyx()[1]



    character = [10,15]
    window.addch(character[0], character[1],"@")
    while True:
        # function to return that no key was pressed after 1000 mile seconds
        window.timeout(3000)
        # get a character, program only continues after type something
        char = window.getch()
        window.clear()
        window.border(0)
        if char == curses.KEY_UP:
            character[0] -= 1
        elif char == curses.KEY_DOWN:
            character[0] +=1
        elif char == curses.KEY_LEFT:
            character[1] -= 1
        elif char == curses.KEY_RIGHT:
            character[1] +=1
        else:
            pass
        if character[0] <= 0 or character[0] >= height-1:
            return
        if character[1] <= 0 or character[1] >= width-1:
            return
        
        window.addch(character[0], character[1],"@")

    
curses.wrapper(game_loop)
print("perdeu")