# Chapter 2, exercise 3.
import os
import sys
import operator

sys.path.append(os.path.pardir)


import Pmf


def mode(hist):
    """
    Takes a Hist object and returns its most frequent value.

    Using the built-in `max` function, we pass an iterable of all dictionary
    items and an `operator.itemgetter` which will retrieve the value in the
    position `1` of the tuple returned in each iteration. That will calculate
    the maximum value.
    """
    return max(hist.GetDict().iteritems(), key=operator.itemgetter(1))


def main():
    """
    Testing the `mode` function.
    """
    hist = Pmf.MakeHistFromList([1, 2, 2, 2, 2, 5, 7, 9, 9, 4, 3, 6])
    value, frequency = mode(hist)

    print 'The value {0} has the maximum frequency ({1})'.format(value,
                                                                 frequency)

if __name__ == '__main__':
    main()
