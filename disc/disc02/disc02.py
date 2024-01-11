#Currying#
def keep_ints(cond, n):
    """
    Print out all integers 1..i..n where cond(i) is true
    """
    for i in range(1,n+1):
        if cond(i):
            print (i)

def is_even(x):
    return x % 2 == 0

keep_ints(is_even,5)


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
all integers 1..i..n where calling cond(i) returns True.
    """
    def f(cond):
        for i in range(1,n+1):
            if cond(i):
                print (i)
    return f
def is_even(x):
    return x % 2 == 0
make_keeper(5)(is_even)




#Self Reference#
def print_delayed(x):
    """Return a new function. This new function, when called,
will print out x and return another function with the same
behavior
    """
    def delay_print(y):
        print (x)
        return print_delayed(y)
    return delay_print
f = print_delayed(1)
f = f(2)(3)

def print_n(n):
    """Write a function print n that can take in an integer n and returns
a repeatable print function that can print the next n parameters. After the
nth parameter, it just prints ”done”.
    """
    def inner_print(x):
        if n-1<0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

g=print_n(2)
g("first")("second")("third")
