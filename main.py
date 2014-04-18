"""
Python implementation of the matrix information measurement examples from the
StackExchange answer written by WilliamAHuber for
"Measuring entropy/ information/ patterns of a 2d binary matrix"
http://stats.stackexchange.com/a/17556/43909

Copyright 2014 Cosmo Harrigan
This program is free software, distributed under the terms of the GNU AGPL v3.0
"""

__author__ = 'Cosmo Harrigan'

from matplotlib import pyplot
from neighborhood_functions import avg_components
from moving_window_filter import moving_window_filter
from calculate_profile import profile

# Function to apply
F = avg_components

# Define the matrices as input_matrices
from data import *

# Iterate over the input matrices
for m in range(0, len(input_matrices)):
    active_matrix = input_matrices[m]
    print "---------\nMatrix #{0}\n---------\n".format(m)

    # Produce the filtered matrices at varying scales and the associated
    # entropy "profiles"
    matrices = []
    for n in range(1, min(active_matrix.shape)):
        output_matrix = moving_window_filter(matrix=active_matrix,
                                             f=F,
                                             neighborhood_size=n)
        matrices.append(output_matrix)
        subplot = pyplot.subplot(5, 4, m * 4 + n)
        pyplot.axis('off')
        pyplot.imshow(output_matrix,
                      interpolation='nearest',
                      cmap='Greys_r',
                      vmin=0,
                      vmax=1)
        print "Neighborhood size = {0}\n{1}\n".format(n, output_matrix)

    print "Profile:\n{0}\n".format(profile(matrices))

pyplot.show()
