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
	if pyautogui.locateOnScreen('images/stage_1_id.PNG') != None:
		return 1
	if pyautogui.locateOnScreen('images/stage_2_id.PNG') != None:
		return 2
	else:
		return 0


	



#check stage before each stop, make a function that looks for identifiers on the screen
#then carries out the appriate check

stage = 0
stage = stageIdentify()
print("returned stage: ",stage)



