def fibonacci_calc(term): 
    result = ((((1.6180339)**term)) - ((1 - 1.6180339)**term)) / (5**(1/2))
    result = round(result)
    return result

def fibonacci_recur(term):
    if term == 0:
        return 0
    if term == 1:
        return 1
    return fibonacci_recur(term - 1) + fibonacci_recur(term - 2)

print(fibonacci_calc(9))
print(fibonacci_recur(9))