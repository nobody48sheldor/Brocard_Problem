from math import *
import numpy as np

n = int(input("n = "))

x = np.linspace(0, n, n+1)

def factorial(n):
    s = []
    for i in range(len(n)):
        s.append(np.math.factorial(n[i]) + 1)
    return(s)

def square(n):
    s = n**2
    return(s)

f = factorial(x)
s = square(x)

print("done")

u = 0
v = 0
while u < n:
    v = 0
    while v < n:
        if f[u] == s[v]:
            print("fact(",u,") = ", v,"^2 = ", f[u])
        v = v + 1
    u = u + 1
