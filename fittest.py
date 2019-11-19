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
