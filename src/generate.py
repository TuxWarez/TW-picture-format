from PIL import Image
import argparse, binascii, os, gzip, shutil

parser = argparse.ArgumentParser(description="Arguments")
parser.add_argument("-bg", "--background", default=0, type=str, help="Background dec color eg. 26,234,5")
parser.add_argument("-fg", "--foreground", default=0, type=str, help="Foreground dec color eg. 26,234,5")
parser.add_argument("-img", "--image", default="", type=str, help="Image file to convert")
args = parser.parse_args()

im = Image.open(args.image)
file = open("image.txt", "w")
res1, res2, res3 = 0, 0, 0
pixels = im.load()
background = args.background.split(","); background = [int(x) for x in background]
foreground = args.foreground.split(","); foreground = [int(x) for x in foreground]
image_file = args.image

with Image.open(args.image) as img:
    width, height = img.size

width_array = [int(bit) for bit in f"{(int(width/8)):012b}"]
height_array = [int(bit) for bit in f"{height:012b}"]
width_array.reverse(); height_array.reverse()
size_array = width_array + height_array

for i in range(8):
    res1 += size_array[i] * pow(2, i)
for i in range(8):
    res2 += size_array[i + 8] * pow(2, i)
for i in range(8):
    res3 += size_array[i + 16] * pow(2, i)

file.write( f"{res1:02x}{res2:02x}{res3:02x}")
for i in background:
    file.write(f"{i:02x}")
for i in foreground:
    file.write(f"{i:02x}")
for i in range(height):
    for j in range(int(width/8)) :
        pixel_bar = []
        power = 0
        for k in range(8):
            value = pixels[(j*8) + k, i]
            if not isinstance(value, int):
                if abs(foreground[0] - value[0]) < abs(background[0] - value[0]) and abs(foreground[1] - value[1]) < abs(background[1] - value[1]) and abs(foreground[2] - value[2]) < abs(background[2] - value[2]):
                    value = 0
                else:
                    value = 1
            power += value * pow(2, (7-k))
        file.write(f"{power:02x}")
file.close()

binstr = binascii.unhexlify(open("image.txt").read())
with open("output.bin", "wb") as binary_file:
    binary_file.write(binstr)
os.remove("image.txt")

with open("output.bin", "rb") as f_in:
    with gzip.open("output.tw", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
os.remove("output.bin")
