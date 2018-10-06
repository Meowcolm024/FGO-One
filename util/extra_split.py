from PIL import Image


def extra_split():
    im2 = Image.open("./temp/2.png")
    img2_size = im2.size
    x = img2_size[0] / 5
    y = img2_size[1] / 7
    region = im2.crop((2 * x, 2 * y, 3 * x, 3 * y))
    region.save("./temp/s1.png")
