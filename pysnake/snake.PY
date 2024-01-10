import pandas as pd
import curses
import random
import os
from datetime import datetime

def main():

    # menu
        # start
            # start game
            # when you lose
                # ask if user want to save score
                # play again
                # return to menu.
        # ranking
            # "show top 5"
            # return to menu
            # reset score
                # yes to confirm and return to menu.
                # no to return
        # quit
        

    curses.wrapper(game_loop)
    print('you lose')
    print(f"your score is {fruit_count} fruits")
    score = pd.read_csv("pysnake\scores.csv")
    save_score = input("would you like to save your score? [y][n]")
    if save_score == "y":
        name = input("name")
        current_directory = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_directory, "scores.csv")
        score = pd.read_csv(file_path, index_col=0)
        new_score = {"date":[datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "name":[name], "score":[fruit_count]}
        df = pd.DataFrame(new_score)
        score = pd.concat([score, df],ignore_index=True,axis=0)
        score.to_csv(file_path)





def game_loop(window):
    # Initial setup
    curses.curs_set(0)
    snake = [[10,15],[10,16],[10,17],[10,18]]
    head = snake[0].copy()
    fruit=[1,2]
    keepdirection = None
    fruit_location(window, fruit, snake)
    global fruit_count 
    fruit_count = 0
    # loop start
    while True:
        draw_screen(window)
        draw_actor(snake, window)
        draw_fruit(window, fruit)
        head = snake[0].copy()
        direction = get_new_direction(window, timeout = 100)
        if oposite_direction(direction,snake, head) == True:
            direction = None

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
        if head in snake:
            return
        update_snake(snake,head,fruit)
        if fruit in snake:
            snake.insert(0,head)
            fruit_count +=1
            fruit_location(window, fruit, snake)
        


def oposite_direction(direction, snake, head):
    fake_head = head.copy()
    if direction == None:
        return
    else:
        move_actor(fake_head, direction)
        if fake_head == snake[1]:
            return True


def fruit_location(window, fruit, snake):
    while True:
        height = window.getmaxyx()[0]
        width = window.getmaxyx()[1]
        y = random.randint(2, height-2)
        x = random.randint(2, width-2)
        fruit[0]=y
        fruit[1]=x
        if fruit in snake:
            continue
        else:
            break
def draw_fruit(window, fruit):
    window.addch(fruit[0], fruit[1], curses.ACS_DIAMOND)
    window.refresh()
            
def update_snake(snake,head,fruit):
    if fruit in snake:
        snake.insert(0,head)
    else:
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
    if direction in [450,456,454,452, curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT,curses.KEY_RIGHT]:
         return direction
    else:
         return None

def move_actor(actor, direction):
    #arrow up
    if direction == 450 or direction == curses.KEY_UP:
            actor[0] -= 1
    # arrow down
    elif direction == 456 or direction == curses.KEY_DOWN:
        actor[0] +=1
    # arrow left
    elif direction == 452 or direction == curses.KEY_LEFT:
        actor[1] -= 1
    # arrow right
    elif direction == 454 or direction == curses.KEY_RIGHT:
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
    main()


    


