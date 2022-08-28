import math
from random import uniform
import matplotlib.pyplot as plt

def ok(r, d):
    R = abs(r)
    D = abs(d)
    if D >= R:
        return 0
    else:
        return 1 - (D/R)**1.5

class VectorModel():
    def __init__(self, start_func=lambda x: 0,
                 force=lambda l,d: l, #*(1+abs(l))/(1+abs(l)+abs(d)),
                 miradus=lambda r,d: ok(r, d),
                 radonus=500,
                 radionus=lambda r,epoch,epochs:r * (epochs-epoch)/epochs):
        self.start_func = start_func
        self.force = force
        self.miradus = miradus
        self.radonus = radonus
        self.radionus = radionus
        self.vectors = [] # (x0, l, r)

    def run(self, x):
        y = self.start_func(x)
        for v in self.vectors:
            x0, l, r = v
            d = x - x0
            y += self.force(l, d)*self.miradus(r, d)
        return y

    def train(self, points, epochs=1, show=False):
        for epoch in range(epochs):
            r = self.radionus(self.radonus, epoch, epochs)
            for point in points:
                x0, y0 = point
                y1 = self.run(x0)
                l = y0 - y1
                self.vectors.append((x0, l, r))
        if show:
            plt.style.use('seaborn-whitegrid')
            fig, ax = plt.subplots()
            X = [p[0] for p in points]
            Y = [p[1] for p in points]
            mx, mn = max(X), min(X)
            k = (30/(mx - mn + 10))
            X1 = [i/k for i in range(int((mn-5)*k), int((mx+5)*k))]
            Y1 = [self.run(x) for x in X1]
            ax.plot(X1,Y1)
            ax.scatter(X, Y)
            plt.show()


