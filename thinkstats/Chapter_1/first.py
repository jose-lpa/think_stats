import os
import sys

sys.path.append(os.path.pardir)

import survey


table = survey.Pregnancies()
table.read_records()
print 'Number of pregnancies: {0}'.format(len(table.records))


# 2nd exercise
live = sum(1 for r in table.records if r.outcome == 1)
print 'Live birhs: {0}'.format(live)


# 3rd exercise
firsts = []
others = []

# Collect the live births
for record in table.records:
    if record.outcome == 1:
        if record.birthord == 1:
            firsts.append(record)
        else:
            others.append(record)

print 'First babies: {0}'.format(len(firsts))
print 'Other babies: {0}'.format(len(others))


# 4th exercise
firsts_average = float(sum(r.prglength for r in firsts)) / len(firsts)
others_average = float(sum(r.prglength for r in others)) / len(others)

print 'Average pregnancy weeks for first babies: {0}'.format(firsts_average)
print 'Average pregnancy weeks for other babies: {0}'.format(others_average)

difference_days = (firsts_average - others_average) * 7.0

print 'Difference in days: {0}'.format(difference_days)
print 'Difference in hours: {0}'.format(difference_days * 24.0)
