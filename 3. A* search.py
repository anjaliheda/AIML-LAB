import numpy as np
from queue import PriorityQueue

def get_moves(state):
    """Returns possible moves by swapping the empty tile (0) with adjacent tiles."""
    zero_pos = np.argwhere(state == 0)[0]  # Find empty tile position
    moves = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
    
    for d in directions:
        new_pos = zero_pos + d
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:  # Stay within bounds
            new_state = state.copy()
            new_state[zero_pos[0], zero_pos[1]], new_state[new_pos[0], new_pos[1]] = \
                new_state[new_pos[0], new_pos[1]], new_state[zero_pos[0], zero_pos[1]]
            moves.append(tuple(map(tuple, new_state)))  # Convert to tuple for hashing
    return moves

def heuristic(state, goal_state):
    """Counts misplaced tiles as heuristic."""
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j])

def solve_puzzle(initial_state, goal_state):
    """A* search to find the shortest path from initial to goal state."""
    queue = PriorityQueue()
    queue.put((0, tuple(map(tuple, initial_state)), []))  # Store as tuple for hashing
    visited = set()

    while not queue.empty():
        cost, state_tuple, path = queue.get()
        
        if state_tuple == tuple(map(tuple, goal_state)):  # Goal reached
            return path + [state_tuple]
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for move in get_moves(np.array(state_tuple)):
            queue.put((len(path) + 1 + heuristic(move, goal_state), move, path + [state_tuple]))

    return None  # No solution found

# Get user input
print("Enter initial state row-wise (space-separated, 0 for blank):")
initial_state = np.array([list(map(int, input().split())) for _ in range(3)])
print("Enter goal state row-wise:")
goal_state = np.array([list(map(int, input().split())) for _ in range(3)])

# Solve puzzle
solution = solve_puzzle(initial_state, goal_state)

# Print result
if solution:
    for step in solution:
        print(np.array(step), "\n")
    print("Number of moves:", len(solution) - 1)
else:
    print("No solution found.")
