#===============================================================================
#
#     Modal Tool Kit (MTK)
#
#     Copyright 2017 Christopher A. Lupp
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#===============================================================================

# distutils: language = c++

# Cython imports
from libcpp cimport bool
from libcpp.vector cimport vector
from libcpp.string cimport string

# Eigency
from eigency.core cimport *

from MTK.Core cimport EigenPair as cppEigenPair
from MTK.Core cimport ModeSet as cppModeSet


# EigenPair (wrapper)
cdef class EigenPair:
    cdef cppEigenPair[double] ptr


# ModeSet (wrapper)
cdef class ModeSet:
    cdef cppModeSet[double] ptr