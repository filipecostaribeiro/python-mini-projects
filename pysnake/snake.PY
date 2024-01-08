import curses

def game_loop(window):
    personagem = [10,15]
    window.addch(personagem[0], personagem[1],"@")
    while True:
        # function to return that no key was pressed after 1000 mile seconds
        window.timeout(3000)
        # get a character, program only continues after type something
        char = window.getch()
        window.clear()
        if char == curses.KEY_UP:
            personagem[0] -= 1
        elif char == curses.KEY_DOWN:
            personagem[0] +=1
        elif char == curses.KEY_LEFT:
            personagem[1] -= 1
        elif char == curses.KEY_RIGHT:
            personagem[1] +=1
        else:
            pass
        window.addch(personagem[0], personagem[1],"@")

  

curses.wrapper(game_loop)