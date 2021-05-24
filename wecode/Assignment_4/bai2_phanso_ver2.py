def ComputeGCD(x, y):
    if x == 1 or y == 1:
        return 1
    while y:
        x, y = y, x % y
    return x


class NFraction:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.frac1 = a / b
        self.frac2 = c / d

    def Transform(self):
        count = 0
        while True:
            count += 1
            self.a += 1
            self.b += 1
            x = ComputeGCD(self.a, self.b)
            self.a /= x
            self.b /= x
            # print(self.a, self.b)
            if self.a == self.c and self.b == self.d:
                self.a = int(self.a)
                self.b = int(self.b)
                return count
            if self.a == 1 and self.b == 2:
                self.a = int(self.a)
                self.b = int(self.b)
                return count

    def Solve(self):
        if self.frac1 < self.frac2:
            temp = self.Transform()
            if self.a == self.c and self.b == self.d:
                return temp
            elif self.d - self.c == 1:
                return temp + self.d - self.b
            else:
                return 0
        else:
            return 0


a = int(input())
b = int(input())
c = int(input())
d = int(input())

s = NFraction(a, b, c, d)
print(s.Solve())