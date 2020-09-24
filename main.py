import numpy as np
import cv2
import pyautogui
import time
import pytesseract
#REMEMBER:
#WHEN USING THIS PROGRAM LEAGUE NEEDS TO BE AT 1600 X 900 RES AS THIS IS THE RESOLUTION OF THE 
#REFERENCE IMAGES USED FOR AUTOGUI. 


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


