import curses
 
def game_loop(window):
    # Initial setup
    curses.curs_set(0)
    window.border(0)
    character = [10,15]
    window.addch(character[0], character[1],"@")
    # loop start
    while True:
        draw_screen(window)
        draw_actor(character, window)
        direction = get_new_direction(window, timeout = 1000)
        if direction != None:
            move_actor(character, direction)
        if actor_hit_border(character,window):
            return


def draw_screen(window):
    """ Prompts a clear window and create a border to play inside."""
    window.clear()
    window.border(0)

def draw_actor(actor, window):
    """ print the actor in its position"""
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)

def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_RIGHT]:
         return direction
    else:
         return None

def move_actor(actor, direction):
    if direction == curses.KEY_UP:
            actor[0] -= 1
    elif direction == curses.KEY_DOWN:
        actor[0] +=1
    elif direction == curses.KEY_LEFT:
        actor[1] -= 1
    elif direction == curses.KEY_RIGHT:
        actor[1] +=1
        
def actor_hit_border(actor, window):
    height = window.getmaxyx()[0]
    width = window.getmaxyx()[1]
    if actor[0] <= 0 or actor[0] >= height-1:
        return True
    if actor[1] <= 0 or actor[1] >= width-1:
        return True
    else:
         return False

if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Perdeu!')
    


