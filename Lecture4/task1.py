# calculator

# def calc_1(a, b):
#     return(a+b)

calc_1 = lambda a, b: a + b

def calc_2(a, b):
    return (a*b)

def math(operation, x, y):
    print(operation(x, y))

math(calc_1, 5, 3)
math(lambda a, b: a+b, 4, 9)