import curses
from snake import return_position, update_snake, move_actor

def test_return_position():
    assert return_position([1, 2, 3, 4, 5], 6) == 1
    assert return_position([11, 8, 5, 3, 2], 10) == 2
    assert return_position([10, 8, 6, 4, 2], 7) == 3
    assert return_position([10, 8, 6, 4, 2], 3) == 5
    assert return_position([10, 8, 6, 4, 2], 1) == 0


def test_update_snake():
    assert update_snake([[10,15],[10,16],[10,17],[10,18]],[9,15],[1,1]) == [[9,15],[10,15],[10,16],[10,17]]

def test_move_actor():
    assert move_actor([5,5],curses.KEY_UP) == [4,5]
    assert move_actor([5,5],curses.KEY_DOWN) == [6,5]
    assert move_actor([5,5],curses.KEY_LEFT) == [5,4]
    assert move_actor([5,5],curses.KEY_RIGHT) == [5,6]

# pytest test_snake.py