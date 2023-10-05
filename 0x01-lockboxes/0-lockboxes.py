def canUnlockAll(boxes):
    # Create a set to keep track of opened boxes.
    opened_boxes = set()
    # Start with the first box open.
    opened_boxes.add(0)
    # Create a stack to perform DFS.
    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        # Check each key in the current box.
        for key in keys:
            if key < len(boxes) and key not in opened_boxes:
                # If the key corresponds to a valid box and that box is not opened, open it.
                opened_boxes.add(key)
                stack.append(key)

    # Check if all boxes have been opened.
    return len(opened_boxes) == len(boxes)

