#!/usr/bin/python3

"""
Copyright (C) 2019  Christian Schärf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from tfast import TitrationVolume
from titration import CalcVol
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
from time import monotonic
from sys import argv


def read_xy_file(filename):
    f = open(filename, "r")
    x = []
    y = []
    for l in f:
        if not l.startswith("#"):
            s = l.split(" ")
            x.append(float(s[0]) / 1000)
            y.append(float(s[1]))

    f.close()
    return np.array(x), np.array(y)


class TWrapper(CalcVol):
    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, c0_b, *args):
        return [CalcVol.__call__(self, i, *args) for i in c0_b]


class TWrapperFast(TitrationVolume):
    def __init__(self, *args):
        super().__init__(*args)

    def __call__(self, c0_b, *args):
        return [TitrationVolume.__call__(self, i, *args) for i in c0_b]


def main():
    x, y = read_xy_file(argv[1] if len(argv) > 1 else "data.xy")
    plt.scatter(1000*x, y, marker="+")

    pKs = (2.16, 7.21, 12.32) # Phosphorsäure
    #pKs = (-3, 1.9) # Schwefelsäure

    #t = TWrapper(0.3, 0.1, pKs)
    #start = monotonic()
    #popt, _ = optimize.curve_fit(t, x, y, p0=(0.2, ), bounds=(0, np.inf))
    #interval = monotonic() - start

    t_fast = TWrapperFast(0.3, 0.1, pKs)
    #start = monotonic()
    popt_fast, _ = optimize.curve_fit(t_fast, x, y, p0=(0.2, ), bounds=(0, np.inf))
    #interval_fast = monotonic() - start
    print(popt_fast)
    #print(interval, interval_fast, interval / interval_fast)

    x_fit = np.linspace(0, x[-1], 500)
    plt.plot(1000*x_fit, t_fast(x_fit, *popt_fast))

    plt.xlabel("V(NaOH) [ml]")
    plt.ylabel("pH")
    plt.show()


if __name__ == "__main__":
    main()
