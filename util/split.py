from PIL import Image
from config import screenshot_path


def init():
    im2 = Image.open(f"../{screenshot_path}")
    img2_size = im2.size
    print("width % height: {}".format(img2_size))
    gap = (img2_size[0] - 1920) / 2
    left = gap
    right = img2_size[0] - gap
    top = (img2_size[1] / 2) - 100
    bottom = img2_size[1]
    print((left, top, right, bottom))
    region = im2.crop((left, top, right, bottom))
    region.save("../temp/out.png")


def main():
    im = Image.open("../temp/out.png")
    img_size = im.size
    xx = 5
    yy = 1
    x = img_size[0] // xx
    y = img_size[1] // yy
    for j in range(yy):
        for i in range(xx):
            left = i*x
            up = y*j
            right = left + x
            low = up + y
            region = im.crop((left, up, right, low))
            print((left, up, right, low))
            region.save(f"../temp/{i}.png")


init()
main()
