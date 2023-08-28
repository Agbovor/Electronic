from functools import reduce

def add(x,y):
    return x + y
numbers = [1,2,3,4,5,6,7,8,9]
print(reduce(add,numbers))

def sub(x,y):
    return x - y
numbers = [1,2,3,4,5,6,7,8,9]
print(reduce(sub,numbers))

def div(x,y):
    return x + y
numbers = [1,2,3,4,5,6,7,8,9]
print(reduce(div,numbers))