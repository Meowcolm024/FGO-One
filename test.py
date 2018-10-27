from interface.Major import Major
from phantasms.detection import match_np

"""
s = Major()
out = s.recognize()
print(out)
"""


from util.split import split
from util.cvs import check
from extra.matching import matching
from phantasms.turns import get_turns

split()

exists = [i for i in range(5)]
for exist in exists:
    tmp = f"./temp/s{exist}.png"
    for exis in exists:
        if exist != exis:
            pic = f"./temp/{exis}.png"
            if check(pic, tmp, 0.9) == 1:
                exists.remove(exis)

np = []
for i in range(3):
    for j in exists:
        if check(f"./temp/np{i}.png", f"./temp/s{j}.png", 0.75) == 1:
            np.append(i)

print(np)
print("--------")
a = matching()
for i in range(5):
    print(a[i].chain)
print("--------")
get_turns()
print("--------")
match_np()
