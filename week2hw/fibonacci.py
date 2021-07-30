def fibonacci_calc(term): 
    result = ((((1.6180339)**term)) - ((1 - 1.6180339)**term)) / (5**(1/2))
    result = round(result)
    return result

print(fibonacci_calc(2))