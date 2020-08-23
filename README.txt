UNFINISHED


Project idea/purpose
-gets the player into a game of ARAM from the search screen into the match
-current:
	uses pyautogui to accept matches
	uses pytesseract to attempt regonition of the character your playing
	attempts to use this to find character name in a dictionary of characters which relates to the mastery page you want to use on them
	


libarys used in this:
install the following to an enviroment

python 3.8


opencv
numpy - comes with opencv when you pip install
"pip install opencv-python"
only standard libary used here



pyautogui
"pip install pyautogui"

pytesseract 
"pip install pytesseract"

(a wrapper for python )

this requires the isntallation of the google command line application tesseract

https://pypi.org/project/pytesseract/




FuzzyWuzzy 
pip install FuzzyWuzzy
this is for fuzzy word detection as the readings from tesseract are not 100% acurate
https://www.datacamp.com/community/tutorials/fuzzy-string-python





