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
print(f"The maxima is at x = {max_x}\nThe maximum value obtained is {max_val}")
