#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from time import monotonic
from tfast import Titration, TitrationVolume
#from matplotlib.backends.backend_qt5cairo import FigureCanvasQTCairo as FigureCanvas

Kw = 1e-14
epsilon = 1e-8


class Calc:
    def __init__(self, pKs):
        self.Ks = [pow(10, -i) for i in pKs]
        self.result_cache = []

    def __call__(self, c0_b, c0_s):
        HA = 1
        A = [1] * len(self.Ks)

        if len(self.result_cache):
            HA, A[0] = self.find_closest_result(c0_s, c0_b)

        while True:
            while True:
                H = self.Ks[0] * HA / A[0]
                for i, Ks in enumerate(self.Ks[1:]):
                    A[i + 1] = Ks * A[i] / H
                OH = Kw / H

                el = (H + c0_b) / (sum((i + 1) * c for i, c in enumerate(A)) + OH)
                if abs(el - 1) < epsilon:
                    break
                A[0] *= np.sqrt(el)

            x = c0_s / (HA + sum(A))
            #print(x)
            if abs(x - 1) < epsilon:
                self.result_cache.append((c0_s, c0_b, HA, A[0]))
                return -(np.log(H) / np.log(10))
            HA *= x

    def percentage(self, percentage, c0_s):
        return self.__call__(c0_s * percentage, c0_s)

    def find_closest_result(self, c0_s, c0_b):
        m = min(self.result_cache, key=lambda x: (c0_s - x[0])**2 + (c0_b - x[1])**2)
        return m[2], m[3]


class CalcVol(Calc):
    def __init__(self, V0, c0_b, pKs):
        self.c0_b = c0_b
        self.V0 = V0
        super().__init__(pKs)

    def __call__(self, V_b, n0_s):
        V = self.V0 + V_b
        c_s = n0_s / V
        c_b = self.c0_b * V_b / V
        return super().__call__(c_b, c_s)

    def percentage(self, percentage, n0_s):
        x = self.__call__(percentage * n0_s / self.c0_b, n0_s)
        #print(x)
        return x


def main():
    pKs = (2.16, 7.21, 12.32)
    x = np.arange(0,  3, 0.02)
    c = CalcVol(0.3, 0.1, pKs)

    start = monotonic()
    res = [c(i, 0.1) for i in x]
    slow = monotonic() - start
    plt.plot(x, res)

    v = TitrationVolume(0.3, 0.1, pKs)
    start = monotonic()
    res2 = [v(i, 0.1) for i in x]
    fast = monotonic() - start
    plt.plot(x, res2)

    print(slow/fast)
    plt.show()


if __name__ == "__main__":
    main()
