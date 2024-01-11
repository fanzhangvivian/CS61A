def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+list(branches)

def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1 :
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branches_leaves=[count_leaves(b) for b in branches(t)]
        return sum(branches_leaves)
    
def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])
    
def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs=[increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)
    
def increment(t):
    return tree(label(t)+1,[increment(b) for b in branches(t)])

def print_tree(t,indent=0):
    print('  '*indent+str(label(t)))
    for b in branches(t):
        print_tree(b,indent+1) 

def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n
def fact_times(n,k):
    "Return k*n*(n-1)*...*1"
    if n==0:
        return k
    else:
        return fact_times(n-1,k*n) 

haste=tree('h',[tree('a',[tree('s'),tree('t')]),tree('3')])
numbers=tree(3,[tree(4),tree(5,[tree(6)])])

def print_sums(t,so_far):
    so_far=so_far+label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in  branches(t):
            print_sums(b,so_far)
