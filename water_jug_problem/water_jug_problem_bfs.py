from collections import deque
def problem_bfs():
    jug1 = 4
    jug2 = 3
    goal = 2
    visited = set()
    queue = deque()

    queue.append((0,0))
    visited.add((0,0))
    i = 1
    while queue:
        x,y = queue.popleft()
        print(f"Current state {i}: jug 1: {x}, jug2: {y}")
        i += 1
        if x == goal or y == goal:
            print("Goal reached!")
            return True
        # Possible actions
        actions = [
            (jug1, y),  
            (x, jug2),  
            (0, y),     
            (x, 0),     
            (min(jug1, x + y), max(0, y - (jug1 - x))),  
            (max(0, x - (jug2 - y)), min(jug2, x + y))   
        ]
        for new_x, new_y in actions:
            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))
    print("Goal not reachable.")

if __name__ == "__main__":
    problem_bfs()

