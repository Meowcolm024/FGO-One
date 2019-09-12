from util.cvs import check

# template path
tmpl = "assets/battle/arts.png"

# tested image path
img = "assets/test/t2.jpeg"

# the threshold
threshold = 0.9

# match template
result = check(img, tmpl, threshold)
print(result)
