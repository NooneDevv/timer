import re

def gp_from_uniques(kph):
    return ((1/1365) * 52353902 + (1/1365) * 118773338 + (1/4095) * 614124338) * kph

#print(gp_from_uniques(18))

f = re.search(r'[E][a][t]', 'Eat cake').group()
print(f)