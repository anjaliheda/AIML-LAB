import numpy as np

def hill_climbing(func, x, step=0.01, max_iter=1000):
    for _ in range(max_iter):
        pos, neg = func(x + step), func(x - step)
        if pos > func(x): x += step
        elif neg > func(x): x -= step
        else: break
    return x, func(x)

func_str = input("Enter a function of x: ")
func = lambda x: eval(func_str)
x = float(input("Enter the starting value: "))

max_x, max_val = hill_climbing(func, x)
print(f"The maxima is at x = {max_x}\nThe maximum value obtained is {max_val}") */ 

or

def hill_climbing(func, start, step_size=0.01, max_iterations=1000):
    current = start
    current_val = func(current)
    
    for _ in range(max_iterations):
        pos = current + step_size
        neg = current - step_size
        pos_val = func(pos)
        neg_val = func(neg)
        
        # Move in the direction that increases the value the most.
        if pos_val > current_val and pos_val >= neg_val:
            current, current_val = pos, pos_val
        elif neg_val > current_val and neg_val > pos_val:
            current, current_val = neg, neg_val
        else:
            break  # No improvement found.
    
    return current, current_val

if __name__ == '__main__':
    # Get the function as a string from the user.
    func_str = input("Enter a function of x (e.g., '-(x-3)**2 + 10'): ")
    # Convert the string to a function using eval (note: eval can be dangerous in real applications).
    f = lambda x: eval(func_str)
    
    # Get the starting value.
    start = float(input("Enter the starting value: "))
    
    maximum, max_value = hill_climbing(f, start)
    print(f"The maximum is at x = {maximum}")
    print(f"The maximum value is {max_value}")
