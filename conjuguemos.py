## USE THE VARIABLES HERE TO CONTROL HOW THE PROGRAM OPERATES ##

# The correct answer (see the GitHub page for more information):
CORRECT = 'hackeo'
# An incorrect answer; this can be anything, it really doesn't matter:
INCORRECT = 'incorrecto'
# Coutdown time (in seconds) at the beginning of the program, used to give you time to select the input box
COUNTDOWN = 5
# The error rate of the program (as a percentage). For example, a value of 0.25 will result in close to a 75% score. Note that this is probability-based, so the actual score may vary:
ERROR_RATE = 0.25
# Number of questions
QUESTIONS = 50

## IGNORE EVERYTHING BELOW THIS LINE ##

import time
import random
import pyautogui

print('Conjuguemos Hack by Leo Wilson (github.com/leomwilson)');
print('This is for educational purposes only. If you use this to get out of doing homework, I\'m not responsible')
for i in range(0,COUNTDOWN):
	print('Starting in ' + str(COUNTDOWN - i) + '...')
	time.sleep(1)
for i in range(0,QUESTIONS):
	if(random.random() < ERROR_RATE):
		pyautogui.typewrite(INCORRECT)
		pyautogui.press('enter')
		pyautogui.hotkey('ctrl', 'backspace')
	else:
		pyautogui.typewrite(CORRECT)
		pyautogui.press('enter')
	print('Totally didn\'t hack #' + str(i))
print('Done.')