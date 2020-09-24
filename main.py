import numpy as np
import cv2
import pyautogui
import time
import pytesseract
#REMEMBER:
#WHEN USING THIS PROGRAM LEAGUE NEEDS TO BE AT 1600 X 900 RES AS THIS IS THE RESOLUTION OF THE 
#REFERENCE IMAGES USED FOR AUTOGUI. 


#--------------------------------------image maninuplation-------------------------------------
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

def rescale(image,scale_percent):
	#scale_percent 220 would be 120% bigger
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	#resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	return resized
#-----------------------------------------------------------------------------------------------



def character_detection():
	#write function to cut image and feed into here
	
	#custom white list adds all upper and lowercase characters (prevents random characters increasing accuracy)
	#--psm 6 means that text is assumed to be in a single line
	custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
	#print(pytesseract.image_to_string(img, config=custom_config))
	
	img = cv2.imread('caitlyn_skin1.png')

	big = rescale(img,250)
	big = get_grayscale(big)
	big = thresholdingBW(big)
	big = dilate(big)
	big = erode(big)
	big = canny(big)
	
	return(pytesseract.image_to_string(big,config=custom_config))




#-------------------------------stage detection--------------------------------
def findAcceptButton():
	print("finding Accept button")
	try:
		pyautogui.click('images/accept.PNG')
	except:
		print("ERROR:AcceptButton not found")
		return False
	return True

		

#0: UNDFINED
#1: SEARCHING
#2: CHAMPSELECT	
def stageIdentify():
	if pyautogui.locateOnScreen('images/stage_1_id.PNG') != None:
		return 1
	if pyautogui.locateOnScreen('images/stage_2_id.PNG') != None:
		return 2
	else:
		return 0


	



#check stage before each stop, make a function that looks for identifiers on the screen
#then carries out the appriate check

#main loop -------------------------------------------------------------------
stage = 0
run = True
while run == True:
	
	stage = stageIdentify()
	print("returned stage: ",stage)
	
	if stage == 1:
		if findAcceptButton() == True:
			run = False
		
		stage = 0
		
print("program finished")


