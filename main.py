import numpy as np
import cv2
import pyautogui
import time



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
		
			

searching = True

while searching == True:
	
	if findAcceptButton() == True:
		break
	else:
		time.sleep(5)


print("end program")



