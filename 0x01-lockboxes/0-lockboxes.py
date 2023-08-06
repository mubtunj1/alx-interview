#!/usr/bin/python3

def canUnlockAll(boxes):
    keys = [0]  # Start with the key for the first box (0th index)
    unlocked = set(keys)  # Keep track of unlocked boxes

    # Iterate through the keys
    for key in keys:
        for box in boxes[key]:
            if box not in unlocked:  # If the box hasn't been unlocked yet
                unlocked.add(box)  # Unlock the box
                keys.append(box)  # Add the key(s) from the box to the keys list

    # Check if all boxes have been unlocked
    return len(unlocked) == len(boxes)
