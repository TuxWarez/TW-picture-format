from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Arguments")
parser.add_argument("-bg", "--background", default=0, type=str, help="Background dec color eg. 26,234,5")
parser.add_argument("-fg", "--foreground", default=0, type=str, help="Foreground dec color eg. 26,234,5")
parser.add_argument("-img", "--image", default="", type=str, help="Image file to convert")
args = parser.parse_args()

im = Image.open(args.image)
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
print(f"0x{res1:02x} 0x{res2:02x} 0x{res3:02x}", end=" ")
for i in background:
    print(f"0x{i:02x}", end=" ")
for i in foreground:
    print(f"0x{i:02x}", end=" ")
print()
for i in range(height):
    for j in range(int(width/8)) :
        pixel_bar = []
        power = 0
        for k in range(8):
            value = pixels[(j*8) + k, i]
            if value[0] == foreground[0] and value[1] == foreground[1] and value[2] == foreground[2]:
                value = 0
            else:
                value = 1
            pixel_bar.append(value)
        pixel_bar.reverse()
        for p in range(8):
            power += pixel_bar[p] * pow(2, p)
        print(f"0x{power:02x}", end=" ")
    print()

