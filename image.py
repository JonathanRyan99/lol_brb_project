import numpy as np
import cv2
import pyautogui
import time
import pytesseract

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,3)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#thresholding
def thresholdingBW(image):
    return cv2.threshold(image, 170, 255, cv2.THRESH_BINARY)[1]


#dilation
def dilate(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((3,3),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)




def rescale(image,scale_percent):
	#scale_percent 220 would be 120% bigger
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	return resized



#custom white list adds all upper and lowercase characters (prevents random characters increasing accuracy)
#--psm 6 means that text is assumed to be in a single line
custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
#print(pytesseract.image_to_string(img, config=custom_config))


img = cv2.imread('caitlyn.png')

big = rescale(img,250)
big = get_grayscale(big)
big = thresholdingBW(big)
big = dilate(big)
big = erode(big)
big = canny(big)

cv2.imshow("resized image", big)



print("resized threshold: ")
print(pytesseract.image_to_string(big,config=custom_config))





gray = get_grayscale(img)
cv2.imshow("greyscale image", gray)
print("grey scale: ")
print(pytesseract.image_to_string(gray,config=custom_config))

thresh = thresholdingBW(gray)
cv2.imshow("threshold image", thresh)
print("threshold: ")
print(pytesseract.image_to_string(thresh,config=custom_config))

cv2.waitKey(0)