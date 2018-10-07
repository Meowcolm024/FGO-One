from PIL import Image


def extra_split():
    for i in range(5):
        im2 = Image.open(f"./temp/{i}.png")
        img2_size = im2.size
        x = img2_size[0] / 5
        y = img2_size[1] / 7
        region = im2.crop((2 * x, 2 * y, 3 * x, 3 * y))
        region.save(f"./temp/s{i}.png")
