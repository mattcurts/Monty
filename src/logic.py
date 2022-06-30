from queue import PriorityQueue
import random
from turtle import up
from typing import List, Dict

"""
This file can be a nice home for your Battlesnake's logic and helper functions.

We have started this for you, and included some logic to remove your Battlesnake's 'neck'
from the list of possible moves!
"""


def get_info() -> dict:
    """
    This controls your Battlesnake appearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    return {
        "apiversion": "1",
        "author": "mattcurts",  # TODO: Your Battlesnake Username
        "color": "#885588",  # TODO: Personalize
        "head": "silly",  # TODO: Personalize
        "tail": "bolt",  # TODO: Personalize
    }


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_snake = data["you"]  # A dictionary describing your snake's position on the board
    my_head = my_snake["head"]  # A dictionary of coordinates like {"x": 0, "y": 0}
    my_body = my_snake[
        "body"
    ]  # A list of coordinate dictionaries like [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]
    board = data["board"]
    board_height = board["height"]
    board_width = board["width"]
    my_id = my_snake["id"]
    snakes = board["snakes"]
    length = len(my_snake["body"])
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = avoid_hazards(my_head, board, possible_moves)
    possible_moves = _avoid_walls(my_head, possible_moves, board_height, board_width)

    possible_moves = _avoid_self(my_body, possible_moves)

    possible_moves = _avoid_others(my_snake, possible_moves, snakes)
    possible_moves = try_direction(possible_moves, my_body, board, my_id, length)

    # TODO: Step 4 - Find food.
    # Use information in `data` to seek out and find food.
    # food = data['board']['food']

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = ""
    try:
        move = random.choice(possible_moves)
    except:
        best_move = move_fail(my_body, my_head, snakes, board, my_id, 10)
        try:
            move = random.choice(best_move)
            return move
        except:
            best_move = move_fail(my_body, my_head, snakes, board, my_id, 1)
            return move

    # TODO: Explore new strategies for picking a move that are better than random

    print(
        f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}"
    )

    return move





def move_fail(my_body, my_head, snakes, board, my_id, length):
    board_height = board["height"]
    board_width = board["width"]
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = _avoid_walls(my_head, possible_moves, board_height, board_width)
    possible_moves = _avoid_self(my_body, possible_moves)
    possible_moves = _avoid_others(my_head, possible_moves, snakes, my_id)
    possible_moves = avoid_hazards(my_head, board, possible_moves)
    length = 10
    best_move = try_direction(possible_moves, my_body, board, my_id, length)
    return best_move


def try_direction(possible_moves, my_body, board, my_id, length):
    head = my_body[0]
    x = head["x"]
    y = head["y"]
    my_size = len(my_body)
    body_no_tail = my_body[:-1]

    if "up" in possible_moves:
        print("UP CHECK")
        if not avoid_self_trap(board, x, y + 1, my_size, body_no_tail, my_id, length):

            possible_moves.remove("up")

    if "down" in possible_moves:
        print("DOWN CHECK")
        if not avoid_self_trap(board, x, y - 1, my_size, body_no_tail, my_id, length):
            possible_moves.remove("down")

    if "left" in possible_moves:
        print("LEFT CHECK")
        if not avoid_self_trap(board, x - 1, y, my_size, body_no_tail, my_id, length):
            possible_moves.remove("left")

    if "right" in possible_moves:
        print("RIGHT CHECK")
        if not avoid_self_trap(board, x + 1, y, my_size, body_no_tail, my_id, length):
            possible_moves.remove("right")

    return possible_moves


def avoid_self_trap(board, x, y, my_size, my_body, my_id, length):
    hazards = board["hazards"]
    height = board["height"]
    width = board["width"]

    oppoenents_body = []
    for snake in board["snakes"]:
        if snake["id"] != my_id:
            oppoenents_body.extend(snake["body"])

    if (
        {"x": x, "y": y} in hazards
        or {"x": x, "y": y} in my_body
        or {"x": x, "y": y} in oppoenents_body
    ):
        return False

    free_spaces = 0
    queue = []
    counted = [{"x": -1, "y": -1}]
    queue.append((x, y))

    while queue:
        x, y = queue.pop()
        if (
            {"x": x, "y": y} in my_body
            or {"x": x, "y": y} in counted
            or {"x": x, "y": y} in hazards
            or {"x": x, "y": y} in oppoenents_body
        ):
            continue
        else:

            counted.append({"x": x, "y": y})
            free_spaces = free_spaces + 1
            if free_spaces > (length):
                return True
            if x > 0:
                queue.append((x - 1, y))
            if x + 1 < width:
                queue.append((x + 1, y))
            if y + 1 < height:
                queue.append((x, y + 1))
            if y > 0:
                queue.append((x, y - 1))

    if free_spaces > (length):
        return True
    else:
        return False


def avoid_hazards(head, board, possible_moves):
    hazards = board["hazards"]
    possible_moves= head_check(possible_moves,head["x"],head["y"] + 1,hazards,"up")
    possible_moves= head_check(possible_moves,head["x"],head["y"] - 1,hazards,"down")
    possible_moves= head_check(possible_moves,head["x"] + 1,head["y"],hazards,"right")
    possible_moves= head_check(possible_moves,head["x"] - 1,head["y"] ,hazards,"left")
    return possible_moves

def _avoid_others(my_snake, possible_moves, snakes):
    my_id = my_snake['id']
    body = my_snake['body']
    head = body[0]
    for snake in snakes:
        body = snake["body"]
        body = body[:-1]
        if snake["id"] != my_id:
            possible_moves = head_check(possible_moves,head["x"],head["y"] + 1,body,"up")
            possible_moves = head_check(possible_moves,head["x"],head["y"] - 1,body,"down")
            possible_moves = head_check(possible_moves,head["x"] + 1,head["y"],body,"right")
            possible_moves = head_check(possible_moves,head["x"] - 1,head["y"],body,"left")
         
           
    return possible_moves

def head_check(possible_moves,x,y,body,direction):
    if {"x": x, "y": y} in body:
        try:
            possible_moves.remove(direction)
        except:
            pass
    return possible_moves

def _avoid_self(my_body, possible_moves):
    head = my_body[0]
    my_body = my_body[:-1]
    if "up" in possible_moves:
        possible_moves = head_check(possible_moves,head["x"],head["y"] + 1,my_body,"up")
    if "down" in possible_moves:
        possible_moves = head_check(possible_moves,head["x"],head["y"] - 1,my_body,"down")
    if "right" in possible_moves:
        possible_moves = head_check(possible_moves,head["x"] + 1,head["y"],my_body,"right")
    if "left" in possible_moves:
        possible_moves = head_check(possible_moves,head["x"] - 1,head["y"],my_body,"left")
    return possible_moves

def _avoid_walls(my_head: dict, possible_moves: List[str], height: int, width: int) -> List[str]:
    """ "
     my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    height:int the height of the board
    width:int the width of the gameboard


    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    if my_head["x"] == width - 1:
        possible_moves.remove("right")
    elif my_head["x"] == 0:
        possible_moves.remove("left")
    if my_head["y"] == 0:
        possible_moves.remove("down")
    elif my_head["y"] == height - 1:
        possible_moves.remove("up")
    return possible_moves
