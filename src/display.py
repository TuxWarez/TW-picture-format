from PIL import Image
import argparse, gzip, shutil
from pathlib import Path

parser = argparse.ArgumentParser(description="Arguments")
parser.add_argument("-img", "--image", default="", type=str, help="Image file to display")
args = parser.parse_args()
file_path = Path(args.image)
file_path.rename(f"{args.image}.gz")
file_path = Path(f"{args.image}.gz")
file_size = file_path.stat().st_size
with gzip.open(f"{args.image}.gz", 'r') as f_in, open(args.image, 'wb') as f_out:
  shutil.copyfileobj(f_in, f_out)

with open(args.image, "rb") as file:
    binary_data = file.read()

byte_list = list(binary_data)
width, height = 0, 0
byte0bit = [int(bit) for bit in f"{byte_list[0]:08b}"]
byte1bit = [int(bit) for bit in f"{byte_list[1]:08b}"]
byte2bit = [int(bit) for bit in f"{byte_list[2]:08b}"]
byte0bit.reverse(); byte1bit.reverse(); byte2bit.reverse()
size = byte0bit + byte1bit + byte2bit
for i in range(12):
    width += size[i] * pow(2, i)
for i in range(12):
    height += size[i + 12] * pow(2, i)
print(f"Resolution: {width*8}x{height}; Background: #{byte_list[3]:02x}{byte_list[4]:02x}{byte_list[5]:02x}; Foreground: #{byte_list[6]:02x}{byte_list[7]:02x}{byte_list[8]:02x}; size: {(file_size/1024):.2f}kb")

fg_red, fg_green, fg_blue = byte_list[3], byte_list[4], byte_list[5]
bg_red, bg_green, bg_blue = byte_list[6], byte_list[7], byte_list[8]
img = Image.new("RGB", (width*8, height), (bg_red, bg_green, bg_blue))

pixels = img.load()

for y in range(height):
    for j in range(width):
        value = byte_list[((y * width) + j) + 9]
        binary_list = [int(bit) for bit in f"{value:08b}"]
        for p in range(8):
            if binary_list[p] == 1:
                pixels[(j * 8) + p, y] = (fg_red, fg_green, fg_blue)

Path(args.image).unlink(missing_ok=True)
file_path.rename(args.image)
img.show()
