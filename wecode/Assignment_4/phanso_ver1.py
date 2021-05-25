import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 0
f = 0
h = float(c) / d


def gcd(m, n):
    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m % n
    return n


while f < h:
    a = a + 1
    b = b + 1
    e = gcd(a, b)
    a = a / e
    b = b / e
    s = s + 1
    f = float(a) / b
if f == h:
    print(s)
else:
    print(0)
