# Questions on link https://x.com/engineers_feed/status/1889052469713322316?t=QjVh4lZ3kQjWt3QFJQGOFQ&s=19

# Solution
from itertools import product

def generate_expressions():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

    minus_combinations = product(range(5), repeat=len(numbers) - 1)
    expressions = []
    for minus_counts in minus_combinations:
        if sum(minus_counts) == 4:  
            expression = ""
            for i in range(7):
                expression += numbers[i]
                expression += " - " * minus_counts[i]
            expression += numbers[-1]  
            expressions.append(expression)
    
    return expressions


for expr in generate_expressions():
    if eval(expr) == 0:
        print(expr, "= 0")