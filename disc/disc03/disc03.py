def multiply(m,n):
    if n==0:
        return 0
    else:
        return multiply(m,n-1)+m

def hailstone(n):
    if n==1:
        print(n)
        return 1
    elif n%2==0:
        print(n)
        return hailstone(n//2)+1
    else:
        print(n)
        return hailstone(n*3+1)+1

def merge(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    elif n1%10>=n2%10:
        return merge(n1,n2//10)*10+n2%10
    elif n1%10<n2%10:
        return merge(n1//10,n2)*10+n1%10
    
def make_func_repeater(f,x):
    def repeat(times):
        if times<=1:
            return f(x)
        return f(repeat(times-1))
    return repeat

def is_prime(n):
    def prime_helper(prime):
        if n==1:
            return False
        elif n==prime:
            return True
        elif n%prime==0:
            return False
        return prime_helper(prime+1)
    return prime_helper(2)

    