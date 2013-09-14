import os
import sys

sys.path.append(os.path.pardir)

import survey


# 2nd exercise
def live_births(table):
    """
    Returns the live births from the table records.
    """
    return sum(1 for r in table.records if r.outcome == 1)


# 3rd exercise
def collect_live_births(table):
    """
    Splits the live births into two lists: first babies and others.
    """
    firsts = []
    others = []

    for record in table.records:
        if record.outcome == 1:
            if record.birthord == 1:
                firsts.append(record)
            else:
                others.append(record)

    return firsts, others


# 4th exercise
def averages(firsts, others):
    """
    Returns the pregnancy lenght averages for first babies and others.
    """
    firsts_average = float(sum(r.prglength for r in firsts)) / len(firsts)
    others_average = float(sum(r.prglength for r in others)) / len(others)

    return firsts_average, others_average


def main():
    table = survey.Pregnancies()
    table.read_records()

    print 'Number of pregnancies: {0}'.format(len(table.records))

    # 2nd exercise
    live = live_births(table)

    print 'Live birhs: {0}'.format(live)

    # 3rd exercise
    firsts, others = collect_live_births(table)

    print 'First babies: {0}'.format(len(firsts))
    print 'Other babies: {0}'.format(len(others))

    # 4th exercise
    firsts_average, others_average = averages(firsts, others)

    difference_days = (firsts_average - others_average) * 7.0

    print 'Difference in days: {0}'.format(difference_days)
    print 'Difference in hours: {0}'.format(difference_days * 24.0)


if __name__ == '__main__':
    main()
