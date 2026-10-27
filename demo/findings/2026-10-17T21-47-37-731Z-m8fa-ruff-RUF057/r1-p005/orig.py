# Near-miss: rule does not fire on imports or __all__
from math import *
print('pi rounded:', round(pi, 0))
# No trigger: round(pi,0) not integer expr
