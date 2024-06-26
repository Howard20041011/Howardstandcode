"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at the upper left, facing East
    Post-condition: Karel is in the pothole, facing south
    """
    for i in range(3):
        go_in()
        put_99()
        go_out()
def go_in():
    """
    Pre-condition: Karel is at the upper left, facing East
    Post-condition: Karel is in the pothole, facing south
    """
    move()
    turn_right()
    move()
def put_99():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()
def go_out():
    """
    Pre - condition: Karel is in the pothole, facing south
    Post - condition: Karel is at the upper left, facing East
    """
    turn_around()
    move()
    turn_right()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
