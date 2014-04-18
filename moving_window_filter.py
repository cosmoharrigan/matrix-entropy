"""
Copyright 2014 Cosmo Harrigan
This program is free software, distributed under the terms of the GNU LGPL v3.0
"""

__author__ = 'Cosmo Harrigan'

import numpy as np


def moving_window_filter(matrix, f, neighborhood_size):
    """
    Applies a filter function to a matrix using a neighborhood size

    @input matrix The matrix to apply the filter function to
    @input f The filter function, such as average, sum, etc.
    @input neighborhood_size The size of the neighborhood for the function
    application
    """
    matrix_width, matrix_height = matrix.shape

    output_matrix = np.zeros([matrix_width - neighborhood_size + 1,
                              matrix_height - neighborhood_size + 1])

    for (row_num, col_num), value in np.ndenumerate(matrix):
        # Check if it already arrived at the right-hand edge as defined by the
        # size of the neighborhood box
        if not ((row_num > (matrix_height - neighborhood_size) or
                col_num > (matrix_width - neighborhood_size))):
            # Obtain each pixel component of an (n x n) 2-dimensional matrix
            # around the input pixel, where n equals neighborhood_size
            component_matrix = np.zeros([neighborhood_size, neighborhood_size])

            for row_offset in range(0, neighborhood_size):
                for column_offset in range(0, neighborhood_size):
                    component_matrix[row_offset][column_offset] = \
                        matrix[row_num + row_offset][col_num + column_offset]

            # Apply the transformation function f to the set of component
            # values obtained from the given neighborhood
            output_matrix[row_num, col_num] = f(component_matrix)

    return output_matrix
