
import pyautogui
import time
#make switch statement to derermine the current stage then do the accept shit





def findAcceptButton():
	print("finding Accept button")
	try:
		pyautogui.click('images/accept.png')
		return True
	except:
		print("ERROR:AcceptButton not found")
		
			


def findStage():
	if pyautogui.locateOnScreen('images/stage_1_id.png'):
		print("stage 1 found")
		return 1
		

	if pyautogui.locateOnScreen('images/stage_2_id.png'):
		print("stage 2 found")
		return 2

	else:
		print("stage unidentified")
		return 0

	

searching = True
stage = 0

while searching:
	if stage == 0:
		stage = findStage()
	else:
		if stage == 1:
			findAcceptButton()
		if stage == 2:
			print("in lobby call detection...")



