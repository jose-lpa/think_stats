import os
import sys

sys.path.append(os.path.pardir)

import survey


table = survey.Pregnancies()
table.read_records()
print 'Number of pregnancies: {0}'.format(len(table.records))

