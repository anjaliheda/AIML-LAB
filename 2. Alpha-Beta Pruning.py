MAX, MIN = 1000, -1000

def minimax(depth, idx, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[idx]
    
    best = MIN if is_max else MAX
    
    for i in range(2):
        val = minimax(depth + 1, idx * 2 + i, not is_max, values, alpha, beta, max_depth)
        best = max(best, val) if is_max else min(best, val)
        
        if is_max:
            alpha = max(alpha, best)
        else:
            beta = min(beta, best)
        
        if beta <= alpha:
            break  # Alpha-beta pruning
    
    return best

if __name__ == '__main__':
    max_depth = int(input("Enter tree depth: "))
    num_nodes = 2 ** max_depth
    values = [int(input(f"Value for leaf {i+1}: ")) for i in range(num_nodes)]
    
    print("\nOptimal value:", minimax(0, 0, True, values, MIN, MAX, max_depth))
