import os
import sys
import math

sys.path.append(os.path.pardir)

import thinkstats


# Three decorative pumpkins of 1 pound each, two pie pumpkins of 3 pounds each
# and one Atlantic Giant pumpkin of 591 pounds.
weights = (1, 1, 1, 3, 3, 591)

mean, variance = thinkstats.mean_var(weights)

print 'Pumpkins weight mean: {0}'.format(mean)
print 'Pumpkins weight variance: {0}'.format(variance)
print 'Pumpkins weight standard deviation: {0}'.format(math.sqrt(variance))
