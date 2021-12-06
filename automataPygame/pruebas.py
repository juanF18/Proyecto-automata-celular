from typing import BinaryIO
from numpy import random, right_shift

def manual_rule(x):
    if x <= 255 or x >= 0:
        rules = list(np.binary_repr(x, width=8))
        rules.reverse()
    return rules

print(manualrules(30))


rules2=[0,1]
pauseExect = False
rules2=[0,0,0,0,0,0,0,0]
rulesrandom = [random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2), random.choice(rules2)]
a=int("".join(map(str, rules2)),2)
#print(a)