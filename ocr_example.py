import pytesseract
from PIL import Image
#img = Image.open('Van-Cropped.png')
#img.convert('L')
#img = img.save('processed_colored.png')
imagetext = pytesseract.image_to_string(Image.open('Van-Cropped.png'), config='--psm 7')
print(imagetext)

# find the original size of the image to crop the piece that have the text


#processing images with opencv
#import cv2
#img = cv2.imread('flowers.jpg') #RBG 
#cv2.imshow('image', img)
#cv2.waitKey(0)

# grayscale
#img = cv2.imread('chengyi.jpg', 0)
#cv2.imshow('image', img)
#cv2.waitKey(0)


"""img = Image.open("Van.png")
fltWidth, fltHeight = img.size
fltArea = (fltWidth/3-100, fltHeight/6, 2*fltWidth/3+100, fltHeight/3)
img = img.crop(fltArea)
img.save("Van-Cropped.png")"""
