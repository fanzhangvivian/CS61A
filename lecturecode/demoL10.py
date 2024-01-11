def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

def count(s,value):
    total,index=0,0
    while index<len(s):
        element=s[index]
        if element==value:
            total=total+1
        index=index+1
    return total
# 用 for statement 写
def count(s,value):
    total=0
    for element in s:
        if element==value:
            total +=1
    return total

def sum_below(n):
    total=0
    for i in range(n):
        total=total+i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears')

#Sum（recursively） list和recursion的结合
# 求list之和
def mysum(L):
    if L==[]:
        return 0
    else:
        return L[0]+mysum(L[1:])

#求sum（5） >>>1+2+3+4+5 

def sum(n):
    """
    >>>sum(5)
    15
    """
    if n==0:
        return 0
    else:
        return n+sum(n-1)
# 或者采用for循环
def sum(n):
    total=0
    for i in range(n+1):
        total=total+i
    return total

def divisors(n):
    return [1]+[x for x in range(2,n) if n%x==0]
     
def rerverse(str):
    if len(str)==1:
        return str
    else:
        return rerverse(str[1:])+str[0]