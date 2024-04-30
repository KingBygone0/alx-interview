#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list of lists): A list of boxes,
        where each box is represented as a list of integers.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False