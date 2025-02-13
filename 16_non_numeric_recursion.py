###############
## Fibonacci without a dictionary 
#################
def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-2)

print(fib_recur(7))

###############
## Fibonacci with a dictionary 
#################

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:1}
# print(fib_efficient(34, d))

print(fib_efficient(7, d))

