from util.split import split
from extra.extra import get_extra

split()
out = get_extra()
for i in range(len(out)):
    print(out[i].count)
