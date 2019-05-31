import math

class 점:
    def __init__(self, x=0, y=0, 이름=None):
        (self.x, self.y) = (x, y)
        self.이름 = 이름
    def __repr__(self):
        if self.이름:
            return '<점 %s(%d, %d)>' % (self.이름, self.x, self.y)
        return '<점 (%d, %d)>' % (self.x, self.y)
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def 점과의_거리(self, 한_점):
        return math.sqrt(
            (self.x - 한_점.x) ** 2 +
            (self.y - 한_점.y) ** 2
        )

def D(A, B):
    return math.sqrt(
        (A.x - B.x) ** 2 +
        (A.y - B.y) ** 2
    )

def validator(dist, A, B, C):
    if not dist(A, B) >= 0: # 1
        return False
    if not dist(A, B) == dist(B, A): # 2
        return False
    if dist(A, B) == 0: # 3
        if not A == B:
            return False
    if not dist(A, B) + dist(B, C) >= dist(A, B): # 4
        return False
    return True

import random

def random_dots():
    _x = [random.randrange(-100, 100, 1) for _ in range(10)]
    _y = [random.randrange(-100, 100, 1) for _ in range(10)]

    dots = []
    for x in _x:
        for y in _y:
            dots.append(점(x, y))
    random.shuffle(dots)    
    return dots

def main():
    for A in random_dots():
        for B in random_dots():
            for C in random_dots():
                if not validator(D, A, B, C):
                    print(False)
                    exit(0)
    print(True)

if __name__ == '__main__':
    main()
