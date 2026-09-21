# Specs

Max resolution: 32760x4095  
Colors: 2 of your choice  
  
# Instructions

**Linux:**

To convert a picture into the TW format:  
`python image.py -bg [RGB] -fg [RGB] -img [input] > image.txt; xxd -r -p image.txt [output]; rm image.txt`  
  
`python image.py -bg [bgRGB] -fg [fgRGB] -img [input] > image.txt` converts a picture into a text file with hexadecimal digits of the image  
[bgRGB] is background color written in decimals in this format: R,G,B  
[fgRGB] is foreground color written in decimals in this format: R,G,B  
[input] is the filename of the input image  
  
`xxd -r -p image.txt [output]` converts the text file into a binary file  
[output] is the name of the output binary file  
  
`rm image.txt` removes the text file with hex digits  
  
To display images of TW format:  
`python imgdisplay.py -img [input]`
[input] is the filename of TW picture file  
