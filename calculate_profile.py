__author__ = 'Cosmo Harrigan'

from math import log
from collections import Counter


def entropy(probability_list):
    """
    Calculates the entropy of a specified discrete probability distribution

    @input probability_list The discrete probability distribution
    """
    running_total = 0

    for item in probability_list:
        running_total += item * log(item, 2)

    if running_total != 0:
        running_total *= -1

    return running_total


def binary_entropy(p0, p1):
    """
    Calculates the binary entropy given two probabilities

    @input p0 Probability of first value
    @input p1 Probability of second value

    The two values must sum to 1.0
    """
    return entropy([p0, p1])


def matrix_entropy(matrix):
    """
    Calculates the "entropy" of a matrix by treating each element as
    independent and obtaining the histogram of element values

    @input matrix
    """
    counts = dict(Counter(matrix.flatten())).values()
    total_count = sum(counts)
    discrete_dist = [float(x) / total_count for x in counts]
    return entropy(discrete_dist)


def profile(matrices):
    """
    Calculates the "profile" (a list of the entropies) of a set of scaled
    filtered matrices as defined in the StackExchange answer

    @input matrices The set of scaled filtered matrices
    """
    return [matrix_entropy(scale) for scale in matrices]
