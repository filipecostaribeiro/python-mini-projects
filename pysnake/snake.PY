import pandas as pd
import curses
import random
import os
from datetime import datetime
from tabulate import tabulate
import sys

def main():

    while True:
        clear_terminal()   
        menu()
        command = input("Command: ")
        if command == "0":
            curses.wrapper(game_loop)
            score_handle(fruit_count)
        elif command == "1":
            clear_terminal() 
            display_ranking()
            # ranking menu
            print("Return to menu [0]")
            print("Reset ranking [1]\n")
            command = input("Command: ")
            if command == "0":
                continue
            elif command == "1":
                reset_score()
                continue
        elif command == "2":
            clear_terminal()
            sys.exit()



def clear_terminal():
    # Check the operating system and use the appropriate command
    if os.name == 'posix':  # Linux and macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')

def save_score(fruit_count,position):
    name = input("Name: ")
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, "scores.csv")
    score = pd.read_csv(file_path, index_col=0)
    new_score = {"Position":[position], "Name":[name], "Fruits":[fruit_count],"Date":[datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
    df = pd.DataFrame(new_score)
    score = pd.concat([score, df],ignore_index=True,axis=0)
    score = score.sort_values(by="Date", ascending=False).sort_values(by="Fruits", ascending=False)
    score = score.head(5)
    score.reset_index(inplace=True,drop = True)
    score.reset_index(inplace=True)
    score = score.drop('Position', axis=1)
    score.rename(columns={'index': 'Position'}, inplace=True)
    score.Position = score.Position.map(lambda p: p + 1)
    score.to_csv(file_path)



def score_handle(fruit_count):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, "scores.csv")
    df = pd.read_csv(file_path, index_col=0)
    l = df["Fruits"].tolist()
    position = return_position(l,fruit_count)
    if position == 0:
        clear_terminal()
        print(f"You lose, your total points are {fruit_count} and you are not at top 5")
    else:
        clear_terminal()
        print(f"Congratulations you are on the top 5 at position {position}")
        save_score(fruit_count,position)

    

def return_position(score_list, fruit_count):
    size = len(score_list)
    if size <5:
        score_list.append(fruit_count)
        score_list.sort(reverse = True)
        position = score_list.index(fruit_count)
        return position+1
    
    else:
        if fruit_count > min(score_list):
            score_list.append(fruit_count)
            score_list.sort(reverse = True)
            score_list.pop()
            position = score_list.index(fruit_count)
            return position +1
            
        else:
            position = 0
            return position
            





def reset_score():
    blank_df = {"Position":[], "Name":[], "Fruits":[],"Date":[]}
    df = pd.DataFrame(blank_df)
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, "scores.csv")
    df.to_csv(file_path)






def display_ranking():
    # Get the path to the csv file
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, "scores.csv")

    # import the csv file as a dataframe to pandas.
    df = pd.read_csv(file_path, index_col=0)

    # Display the DataFrame using tabulate library
    table = tabulate(df, headers='keys', tablefmt='grid')
    print(table)


def menu():
    snake = r"""
           /^\/^\
         _|__|  O|
\/     /~     \_/ \
 \____|__________/  \
        \_______      \
                `\     \                 \
                  |     |                  \
                 /      /                    \
                /     /                       \\
              /      /                         \ \
             /     /                            \  \
           /     /             _----_            \   \
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~

               """

    print(snake) 
    print("Start [0]")
    print("Ranking [1]") 
    print("Quit [2]\n")   
    


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


    


