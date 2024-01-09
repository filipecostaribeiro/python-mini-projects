import curses
 
def game_loop(window):
    # Initial setup
    curses.curs_set(0)
    snake = [[10,15],[10,16],[10,17],[10,18]]
    head = snake[0].copy()
    keepdirection = None

    # loop start
    while True:
        draw_screen(window)
        draw_actor(snake, window)
        head = snake[0].copy()
        direction = get_new_direction(window, timeout = 100)
        if direction != None:
            move_actor(head, direction)
            keepdirection = direction
        else:
            if keepdirection != None:
                move_actor(head, keepdirection)
            else:
                continue
        if actor_hit_border(head,window):
            return
        update_snake(snake,head)
        



def update_snake(snake,head):
    snake.insert(0,head)
    snake.pop()

def draw_screen(window):
    """ Prompts a clear window and create a border to play inside."""
    window.clear()
    window.border(0)
    window.refresh()

def draw_actor(snake, window):
    """ print the actor in its position"""
    for piece in snake:
        window.addch(piece[0], piece[1], curses.ACS_DIAMOND)
    window.refresh()

def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [450,456,454,452]:
         return direction
    else:
         return None

def move_actor(actor, direction):
    #arrow up
    if direction == 450:
            actor[0] -= 1
    # arrow down
    elif direction == 456:
        actor[0] +=1
    # arrow left
    elif direction == 452:
        actor[1] -= 1
    # arrow right
    elif direction == 454:
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
    print('you lose')
    


