def count_stair_ways(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)
    
def count_k(n,k):
    if n<0:
        return 0
    if n==0 or k==1:
        return 1
    return count_k(n-k,k)+count_k(n,k-1)

def even_weighted(s):
    return [s[i]*i for i in range(len(s)) if i%2==0]

def max_product(s):
    if s==[]:
        return 1
    return max(s[:1] * max_product(s[2:]), max_product(s[1:]))
