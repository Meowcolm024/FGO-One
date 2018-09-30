from util.cvs import location


def filter_crd(sh, tmp, thd):  # get the coordinates of cards/marks
    ary = location(sh, tmp, thd)
    ary.sort()
    for i in range(len(ary)):
        for p in range(1, len(ary) - i):
            for k in range(-5, 5):
                for l in range(-5, 5):
                    if ((ary[i][0] + k) == ary[i + p][0]) and ((ary[i][1] + l) == ary[i + p][1]):
                        ary[i + p] = [0, 0]
    while ary.count([0, 0]) >= 1:
        ary.remove([0, 0])
    return ary
