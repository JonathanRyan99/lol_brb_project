import numpy as np
import cv2
import pyautogui
import time
import pytesseract



def findAcceptButton():
	print("finding Accept button")
	try:
		pyautogui.click('images/accept.png')
		return True
	except:
		print("ERROR:AcceptButton not found")
		
			
def stageIdentify():
	print("assessing stage")


	



#check stage before each stop, make a function that looks for identifiers on the screen
#then carries out the appriate check


searching = False

while searching == True:
	
	if findAcceptButton() == True:
		break
	else:
		time.sleep(5)


print("end program")



