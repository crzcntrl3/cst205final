###################
#Puzzle image quiz#
###################
import random

#Makes the individual slice of the original image
def slice(pic, startX, startY, endX, endY):
  x = abs(startX-endX)
  y = abs(startY-endY)
  slicedPic = makeEmptyPicture(x,y)
  #creates arrays to hold the information of the original and empty images
  originalPixels = []
  slicedPixels = []
  #grabs pixel information of the original image and store it in its corresponding array
  for originalX in range(startX, endX):
    for originalY in range(startY, endY):
      originalP = getPixel(pic, originalX, originalY)
      originalPixels.append(originalP)
  #grabs pixel information of the empty image and store it in its corresponding array
  for slicedX in range(0, x):
    for slicedY in range(0, y):
      slicedP = getPixel(slicedPic, slicedX, slicedY)
      slicedPixels.append(slicedP)
  #uses the zip() to combine the two arrays and steps through each pair in the array
  for combinePixels in zip(originalPixels,slicedPixels):
    #grabs each element of the zipped array
    origPix = combinePixels[0]
    slicedPix = combinePixels[1]
    #sets the color to the empty image
    setColor(slicedPix,getColor(origPix))
  return slicedPic

#Copy function
def arrange(section, whole, placeX, placeY):
  w = getWidth(section)
  h = getHeight(section)
  
  sectionPixels = []
  wholePixels  = []
  
  for secX in range(0, w):
    for secY in range(0, h):
      secP = getPixel(section, secX, secY)
      sectionPixels.append(secP)
  for wholeX in range(placeX, placeX+w):
    for wholeY in range(placeY, placeY+h):
      wholeP = getPixel(whole, wholeX, wholeY)
      wholePixels.append(wholeP)
  for combine in zip(sectionPixels,wholePixels):
    secPix = combine[0]
    wholePix = combine[1]
    setColor(wholePix,getColor(secPix))
  return wholePix

#slices the image into 12 peices
def puzzleSlices(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  sectionArray = []
  
  #First Quater
  section1 = slice(pic,0,0,w/3,h/4)
  section2 = slice(pic,(w/3),0,(w*2)/3,h/4)
  section3 = slice(pic,(w*2)/3,0,w,h/4)
  #Second Quater
  section4 = slice(pic,0,h/4,w/3,(h*2)/4)
  section5 = slice(pic,(w/3),h/4,(w*2)/3,(h*2)/4)
  section6 = slice(pic,(w*2)/3,h/4,w,(h*2)/4)
  #Third Quater
  section7 = slice(pic,0,(h*2)/4,w/3,(h*3)/4)
  section8 = slice(pic,(w/3),(h*2)/4,(w*2)/3,(h*3)/4)
  section9 = slice(pic,(w*2)/3,(h*2)/4,w,(h*3)/4)
  #Fourth Quater
  section10 = slice(pic,0,(h*3)/4,w/3,h)
  section11 = slice(pic,(w/3),(h*3)/4,(w*2)/3,h)
  section12 = slice(pic,(w*2)/3,(h*3)/4,w,h)
  
  #creates an arrays of the image slices
  sectionArray.append(section1)
  sectionArray.append(section2)
  sectionArray.append(section3)
  sectionArray.append(section4)
  sectionArray.append(section5)
  sectionArray.append(section6)
  sectionArray.append(section7)
  sectionArray.append(section8)
  sectionArray.append(section9)
  sectionArray.append(section10)
  sectionArray.append(section11)
  sectionArray.append(section12)
  
  return sectionArray

#Creates the puzzle image
def puzzled(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  section = puzzleSlices(pic)
  
  #Creates an array of 12 numbers 0-11 with no repeats
  r = random.sample(range(12),12)
  print r #for testing purposes
  
  puzzle = makeEmptyPicture(w,h)
  arrange(section[r[0]],puzzle,0,0)
  arrange(section[r[1]],puzzle,w/3,0)
  arrange(section[r[2]],puzzle,(w*2)/3,0)
  
  arrange(section[r[3]],puzzle,0,h/4)
  arrange(section[r[4]],puzzle,w/3,h/4)
  arrange(section[r[5]],puzzle,(w*2)/3,h/4)
  
  arrange(section[r[6]],puzzle,0,(h*2)/4)
  arrange(section[r[7]],puzzle,w/3,(h*2)/4)
  arrange(section[r[8]],puzzle,(w*2)/3,(h*2)/4)
  
  arrange(section[r[9]],puzzle,0,(h*3)/4)
  arrange(section[r[10]],puzzle,w/3,(h*3)/4)
  arrange(section[r[11]],puzzle,(w*2)/3,(h*3)/4)
  
  return puzzle
  
  
  
  