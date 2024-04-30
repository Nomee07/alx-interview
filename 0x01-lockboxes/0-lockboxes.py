#!/usr/bin/python3
"""Module to determine if all lockboxes can be opened."""


def canUnlockAll(boxes):
    """
    Determine if all lockboxes can be opened.

    Args:
        boxes (list): A list of lists representing the lockboxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
