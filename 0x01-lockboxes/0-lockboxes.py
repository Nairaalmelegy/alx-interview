#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
- Prototype: def canUnlockAll(boxes) boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Function that checks if the boxes are lists 
    if so it checks if it can be opened and count it
    """

    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for items in range(1, len(boxes) - 1):
        boxes_checked = False
        for index in range(len(boxes)):
            boxes_checked = items in boxes[index] and items != index
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked

    return True
