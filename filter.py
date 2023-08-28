def even(x):
    return x % 2 == 0
numbers = [ 1,2,3,4,5,6,7,8,9]
print(list(filter(even,numbers)))