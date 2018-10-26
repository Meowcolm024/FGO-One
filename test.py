from interface.Major import Major

"""
s = Major()
out = s.recognize()
print(out)
"""


from util.split import split
from util.cvs import check
from extra.find_servant import get_extra

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
for i in range(1, 4):
    for j in exists:
        if check(f"./temp/np{i}.png", f"./temp/s{j}.png", 0.75) == 1:
            np.append(i)

print(np)

a = get_extra()
print(a)
