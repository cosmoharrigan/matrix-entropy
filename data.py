"""
Copyright 2014 Cosmo Harrigan
This program is free software, distributed under the terms of the GNU LGPL v3.0
"""

import numpy as np

__author__ = 'Cosmo Harrigan'

input_matrices = []

input_matrices.append(np.array([
    [0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0]]))

input_matrices.append(np.array([
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0]]))

input_matrices.append(np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]]))

input_matrices.append(np.array([
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]]))

input_matrices.append(np.array([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]))
