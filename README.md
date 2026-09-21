# Specs

Max resolution: 32760x4095  
Colors: 2 of your choice  
  
# Instructions  
  
To convert a picture into the TW format:  
`python image.py -bg [RGB] -fg [RGB] -img [input] > image.txt; xxd -r -p image.txt [output].tw; rm image.txt; gzip -f [output].tw; mv [output].tw.gz [output].tw`  
  
`python image.py -bg [bgRGB] -fg [fgRGB] -img [input] > image.txt` converts a picture into a text file with hexadecimal digits of the image  
[bgRGB] is background color written in decimals in this format: R,G,B  
[fgRGB] is foreground color written in decimals in this format: R,G,B  
[input] is the filename of the input image  
  
`xxd -r -p image.txt [output].tw` converts the text file into a binary file **MUST END IN .TW**  
[output] is the name of the output binary file  
  
`rm image.txt` removes the text file with hex digits  

`gzip -f [output].tw` compresses the output
  
`mv [output].tw.gz [output].tw` renames file  

To display images of TW format:  
`python imgdisplay.py -img [input]`  
[input] is the filename of TW picture file  
