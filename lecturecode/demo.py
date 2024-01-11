from operator import floordiv,mod
from operator import mul


# L1~L7 Code

1+2
x=5

print(x)
x=5
print(x+5)
print(x)


def square(x):
  
    return mul(x,x)

y=square(square(3))
print(y)



def divide_exact(n,d):
    """return the quotient and remainder of dividing N by D

    >>> q,r=divide_exact(2013,10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n,d),mod(n,d)


q,r=divide_exact(2013,10)
print('q:',q)
print('R:',r)

def absolute_value(x):
    """return the absolute value of x."""
    if x<0:
        return -x
    else:
        return x
    
# Summation via while 
i,total=0,0
while i<3:
    i=i+1
    total = total+i

# Prime factorization
def prime_factors(n):
    while n > 1:
        k =smallest_prime_factor(n)
        n =n // k
        print(k)
def smallest_prime_factor(n):
    k =2
    while n % k != 0:
        k =k + 1
    return k


def f(y):
    while y>3:
        print(y)
        y =y-2
    if y==3:
        print('hi')
        f(7) 

round(5/3)

a=2
z = a>1
if z:
    print(7)
if 12:
    print(8)

from math import pi,sqrt
def area(r,shape_constant):
    assert r>0,'A length must be positive'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)/2)


def sum_naturals(n):
    """Sum the first N natural numbers
    >>>sum_naturals(5)
    15
    """
    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total

def sum_cubes(n):
    """ Sum the first N cubes of natural numbers
    >>> sum_cubes(5)
    225
    """
    total,k=0,1
    while k<=n:
        total,k=total+pow(k,3),k+1
    return total


def identity(k):
    return(k)
def cube(k):
    return pow(k,3)

def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

def sum_natural(n):
    return summation(n,identity)

def sum_cube(n):
    return summation(n,cube)

def make_adder(n):
    """return a function that 
    >>> add_three=make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k+n
    return adder

def if_(c,t,f):
    if c:
        t
    else:
        f
from  math import sqrt

def real_sqrt(x):
    if x>0:
        return sqrt(x)
    else:
        return 0.0
    
def has_big_sqrt(x):
    return x>0 and sqrt(x)>10

def compose1(f,g):
    def composed(x):
        return f(g(x))
    # return lambda x:f(g(x))
def g(x):
    return x*x
def f(x):
    return x+1
# h=compose1(lambda x:x*x,lambda y:y+1)
h= compose1(f,g)
result=h(12)


def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x*x



def repeat(f,x):
    while f(x) !=x:
        x=f(x)
    return x
def g(y):
    return (y+5)//3


def make_adder(n):
    def adder(k):
        return k+n
    return adder

def triple(x):
    return 3 * x 

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

def print_sums(n):
    print(n)
    def f(k):
        return print_sums(n+k)
    return f
print_sums(1)(3)(5)

