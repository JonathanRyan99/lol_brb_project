import numpy as np
import cv2
import pyautogui
import time
import pytesseract


def findMatchButton():
	print("finding findMatch button")
	try:
		pyautogui.click('images/findMatch.png')
	except:
		print("ERROR:MatchButton not found")



def findAcceptButton():
	print("finding Accept button")
	try:
		pyautogui.click('images/accept.png')
		return True
	except:
		print("ERROR:AcceptButton not found")
		
			

def imageToString():
	img_cv = cv2.imread(r'test.png')
	# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
	# we need to convert from BGR to RGB format/mode:
	img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
	print(pytesseract.image_to_string(img_rgb))
	

def prepImage():
	image = cv2.imread('nasus.png')
	grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	cv2.imshow("Original image",image)
	cv2.imshow("Original image",grey)

	cv2.waitKey(0)
	cv2.destroyAllWindows()




#imageToString()
prepImage()

searching = False

while searching == True:
	
	if findAcceptButton() == True:
		break
	else:
		time.sleep(5)


print("end program")



