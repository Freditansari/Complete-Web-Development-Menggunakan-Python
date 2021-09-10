x = 'outside'

def my_functions():
    # x = 'inside '
    global x
    return x

print(my_functions())

print(x)