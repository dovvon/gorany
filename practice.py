def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def recurFact(n):
    if n <= 1:
        return 1
    return n * recurFact(n - 1)

print(fact(1))
print(fact(5))
print(fact(10))

print(recurFact(1))
print(recurFact(5))
print(recurFact(10))