class Result:
    def calculate(self, a, b, c=None):
        if c is None:
            return (a + b) / 2
        else:
            return (a + b + c) / 3

r = Result()
print(r.calculate(80, 90))
print(r.calculate(80, 90, 85))
