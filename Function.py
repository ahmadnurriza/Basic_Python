def square(x):
    return x*x

print square(10)

#You can pass functions around as parameters
def dosomething(f, x):
    return f(x)

print dosomething(square, 3)

print dosomething(lambda x : x*x*x, 3)  #lambda = none function, so we make new function