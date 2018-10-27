import os


def clean_tmp():
    for i in range(5):
        filename = f"./temp/servant{i}.png"
        if os.path.exists(filename):
            os.remove(filename)
