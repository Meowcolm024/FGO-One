from cards.Combat import Combat
from util.clean import clean_tmp
from util.split import split
from interface.Major import Major

clean_tmp()

s = Major()
out = s.recognize()
print(out)
"""
split()
a = Combat()
for crd in a.card_crd:
    print(crd)
"""
