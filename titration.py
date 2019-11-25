#!/usr/bin/python3

import numpy as np

Kw = 1e-14
epsilon = 1e-8


class Titration:
    def __init__(self, pKa):
        self.Ks = [pow(10, -i) for i in pKa]
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
            if abs(x - 1) < epsilon:
                self.result_cache.append((c0_s, c0_b, HA, A[0]))
                return -(np.log(H) / np.log(10))
            HA *= x

    def percentage(self, percentage, c0_s):
        return self.__call__(c0_s * percentage, c0_s)

    def find_closest_result(self, c0_s, c0_b):
        m = min(self.result_cache, key=lambda x: (c0_s - x[0])**2 + (c0_b - x[1])**2)
        return m[2], m[3]
