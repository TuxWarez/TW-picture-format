# Specs

Max resolution: 32760x4095  
Colors: 2 of your choice  
Horizontal resolution **must** be divisible by 8
  
# Instructions  
  
To convert a picture into the TW format:  
`python generate.py -bg [bgRGB] -fg [fgRGB] -img [input]`  
  
[bgRGB] is background color written in decimals in this format: R,G,B  
[fgRGB] is foreground color written in decimals in this format: R,G,B  
[input] is the filename of the input image  

To display images of TW format:  
`python display.py -img [input]`  
[input] is the filename of TW picture file  
