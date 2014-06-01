# Chapter 2 exercise 4
import Pmf


def remaining_lifetime(pmf, age):
    """
    Takes the PMF of lifetimes and an age value. Then computes and represents
    the PMF of the distribution of remaining lifetimes.

    To do so, we create a new PMF and calculate its values by incrementing the
    probability associated with those values in the given PMF which are bigger
    than the given age. The new value itself, in such cases, will be the
    difference between the given PMF value and the given age.
    """
    remaining = Pmf.Pmf()

    for value, probabilty in pmf.Items():
        remaining.Incr(value - age, probability) if value > age

    # Normalize values to make probabilities add up to 1 again.
    remaining.Normalize()

    return remaining


def main():
    """
    With a list of lifetime values, computes the PMF for them. Then calls the
    above `remaining_lifetime` function to calculate the remaining lifetimes.
    """
    lifetimes = [1, 3, 5, 6, 4, 3, 5, 6, 7, 5, 4, 3, 3, 4, 2, 7, 2, 9, 8, 1, 1]

    lifetimes_pmf = Pmf.MakePmfFromList(lifetimes)
    remaining = remaining_lifetime(lifetimes_pmf, 3)

    print remaining


if __name__ == '__main__':
    main()
