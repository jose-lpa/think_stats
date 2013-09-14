# Chapter 2, exercise 2.
import os
import sys
import math

sys.path.append(os.path.pardir)


from Chapter_1 import first
import thinkstats
import survey


def main():
    table = survey.Pregnancies()
    table.read_records()

    # Calculate the first babies and other babies averages.
    firsts, others = first.collect_live_births(table)
    firsts_average, others_average = first.averages(firsts, others)

    # Get the pregnancy lengths for first babies and others.
    firsts_lengths = [r.prglength for r in firsts]
    others_lengths = [r.prglength for r in others]

    # Compute the variance for first babies.
    firsts_var = thinkstats.variance(firsts_lengths, firsts_average)

    # Compute the variance for other babies.
    others_var = thinkstats.variance(others_lengths, others_average)

    # Show standard deviations.
    print 'Standard deviation for first gestations: {0}'.format(math.sqrt(
        firsts_var))
    print 'Standard deviation for other gestations: {0}'.format(math.sqrt(
        others_var))


if __name__ == '__main__':
    main()
