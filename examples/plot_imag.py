"""
    Modal Tool Kit (MTK)

    Copyright 2017 Christopher A. Lupp

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from MTK.MTK import EigenPair, ModeSet, PlotImag

from numpy import linspace, sin
from matplotlib.pyplot import show

N_sets = 5
N_modes = 10

pair = EigenPair()


sets = []

for i in range(N_sets):
    set = ModeSet()

    for j in range(N_modes):
        pair["evalue"] = 0.5 * sin(0.05*(i-10*j)) * 1j
        pair["evector"] = [0.0, 0.0]

        set.AddPair(pair)

    sets.append(set)



var = linspace(0.0, 10.0, N_sets)

# plot the mode sets
PlotImag(var, sets)

show()