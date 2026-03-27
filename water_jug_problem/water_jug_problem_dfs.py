def problem_dfs():
    jug1 = 4
    jug2 = 3
    goal = 2
    visited = set()
    stack = []

    # start with both jugs empty
    stack.append((0,0))
    visited.add((0,0))
    i = 1

    while stack:
        x, y = stack.pop()  # pop from stack instead of popleft
        print(f"Current state {i}: jug1: {x}, jug2: {y}")
        i += 1

        if x == goal or y == goal:
            print("Goal reached!")
            return True

        # Possible actions
        actions = [
            (jug1, y),  # fill 4L
            (x, jug2),  # fill 3L
            (0, y),     # empty 4L
            (x, 0),     # empty 3L
            (min(jug1, x + y), max(0, y - (jug1 - x))),  # pour 3L -> 4L
            (max(0, x - (jug2 - y)), min(jug2, x + y))   # pour 4L -> 3L
        ]

        for new_x, new_y in actions:
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                stack.append((new_x, new_y))  # push to stack

    print("Goal not reachable.")
    return False

if __name__ == "__main__":
    problem_dfs()