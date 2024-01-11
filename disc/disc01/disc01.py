# control If statement

def wears_jacket(temp, raining):
    if temp <60 or raining==True :
        return True
    else:
        return False

# While loops Questions

def is_prime(n):
    """"
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
#ADD
    while n>1:
        k=smallest_factor(n)
        if n//k==1:
            return True
        elif n//k!=1:
            return False
    
def smallest_factor(n):
    k=2
    while n%k!=0:
        k=k+1
    return k 

# Environment Diagrams
def f(x):
    return x
def g(x, y):
    if x(y):
        return not y
    return y

x = 3
x = g(f, x)
f = g(f, 0)