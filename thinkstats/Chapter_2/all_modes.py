# Chapter 2, exercise 3.
import os
import sys
import operator

sys.path.append(os.path.pardir)


import Pmf


def all_modes(hist):
    """
    Takes a Hist object and returns its values in descending order of
    frequency.
    """
    freqs = sorted(hist.GetDict().iteritems(), key=operator.itemgetter(1))

    return freqs[::-1]


def main():
    """
    Testing the `mode` function.
    """
    hist = Pmf.MakeHistFromList([1, 2, 2, 2, 2, 5, 7, 9, 9, 4, 3, 6])
    frequencies = all_modes(hist)

    for value, frequency in frequencies:
        print 'Value: {0}\t Frequency: {1}'.format(value, frequency)


if __name__ == '__main__':
    main()
