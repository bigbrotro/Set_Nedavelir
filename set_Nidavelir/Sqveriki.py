from math import cos, sin, acos, e

def upgrade_range(start, stop, step):
    x = []
    while start < stop:
        start += step
        x.append(start)
    return x




class Comp:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def C(self):
        return complex(self.x,  self.y)


    def strange_step_complex(self, n=2):
        absz = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        fi = acos(self.x / absz)
        if n == 2:
            if self.x == 0 and self.y == 0:
                return 0 + 0j
            z = (absz ** 2) * (cos(2 * fi) + sin(2 * fi) *  1j)
            return z
        else:
            z = (e ** (n * fi*1j)) * absz ** n
            return z



