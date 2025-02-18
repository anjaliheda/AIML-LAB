import numpy as np
from queue import PriorityQueue

class State:
    def __init__(self, state, parent, g):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start state to current state
    
    def __lt__(self, other):
        return False

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def is_goal(self, state):
        return np.array_equal(state, self.goal_state)

    def get_possible_moves(self, state):
        possible_moves = []
        zero_pos = np.argwhere(state == 0)[0]
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
        for d in directions:
            new_pos = zero_pos + d
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_state = state.copy()
                new_state[zero_pos[0], zero_pos[1]], new_state[new_pos[0], new_pos[1]] = new_state[new_pos[0], new_pos[1]], new_state[zero_pos[0], zero_pos[1]]
                possible_moves.append(new_state)
        return possible_moves
    
    def heuristic(self, state):
        return np.count_nonzero(state != self.goal_state)
    
    def solve(self):
        queue = PriorityQueue()
        queue.put((0, State(self.initial_state, None, 0)))
        visited = set()

        while not queue.empty():
            _, current = queue.get()
            if self.is_goal(current.state):
                return current
            for move in self.get_possible_moves(current.state):
                move_state = State(move, current, current.g + 1)
                if str(move_state.state) not in visited:
                    visited.add(str(move_state.state))
                    cost = move_state.g + self.heuristic(move_state.state)  # A* cost function: f(n) = g(n) + h(n)
                    queue.put((cost, move_state))
        return None

def get_user_input():
    try:
        print("Enter initial state row-wise (use space between numbers, 0 for blank):")
        initial_state = np.array([list(map(int, input().split())) for _ in range(3)])
        print("Enter goal state row-wise (use space between numbers, 0 for blank):")
        goal_state = np.array([list(map(int, input().split())) for _ in range(3)])
        
        puzzle = Puzzle(initial_state, goal_state)
        solution = puzzle.solve()
        moves = []
        while solution:
            moves.append(solution.state)
            solution = solution.parent
        for move in reversed(moves):
            print(move, '\n')
        print("Number of moves:", len(moves) - 1)
    except ValueError:
        print("Invalid input. Enter numbers correctly.")

get_user_input()
