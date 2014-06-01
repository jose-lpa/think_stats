# Chapter 2 exercise 5
import os
import sys

sys.path.append(os.path.pardir)

import Pmf


def pmf_mean(pmf):
    """
    Computes the mean of a given PMF object.
    """
    mean = 0.0

    for value, probability in pmf.Items():
        mean += probability * value

    return mean


def pmf_variance(pmf, mean):
    """
    Computes the variance of a given PMF object.
    """
    variance = 0.0

    for value, probability in pmf.Items():
        variance += probability * (value - mean) ** 2

    return variance


if __name__ == '__main__':
    values = [1, 2, 3, 7, 6, 9, 8, 6, 5, 3, 2, 3, 5, 7, 7, 8, 9, 1, 3, 2, 4, 5]
    pmf = Pmf.MakePmfFromList(values)

    mean = pmf_mean(pmf)
    variance = pmf_variance(pmf, mean)

    print('PMF mean: {0}\t PMF variance: {1}'.format(mean, variance))
