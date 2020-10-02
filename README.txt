UNFINISHED


Project idea/purpose
-gets the player into a game of ARAM from the search screen into the match
-current:
	uses pyautogui to accept matches
	uses pytesseract to attempt regonition of the character your playing
	attempts to use this to find character name in a dictionary of characters which relates to the mastery page you want to use on them
	


libarys used in this:
install the following to an enviroment

note you will also need to instal google command line application "tesseract"

python 3.8
opencv - ("pip install opencv-python")
numpy - comes with opencv 
pyautogui- ("pip install pyautogui")
pytesseract- ("pip install pytesseract")
	- this is a wrapper for googles cml tesseract
	- https://pypi.org/project/pytesseract/

FuzzyWuzzy - ("pip install FuzzyWuzzy")
	- https://www.datacamp.com/community/tutorials/fuzzy-string-python


to do:
	-image parsing between function name_region() and OCR_on_name() fails return
	-main loop is not written do to above





