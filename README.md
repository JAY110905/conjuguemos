# conjuguemos
This is for educational purposes only. If this is used to cheat in any way, it's not my fault. You have been warned.<br>
**Note:** This only works with conjugation, not vocab. I'm looking for a way to get it to work, but at the moment the exploit used in this program doesn't exist in that mode.
## Installation
To run this program, you need Python installed on your computer, which you can install from [www.python.org](https://www.python.org/). Once Python is downloaded, you need to run this command:
```
pip install pyautogui
```
This will install `pyautogui`, which is necessary for the program to run. The program is tested for Windows 10, but all software is supposed to be cross-compatible and should work on almost any major operating system.
## Setup for Conjuguemos
The process below is shown in the BETA Conjuguemos. However, it works similarly on the current site, just with slightly different styling. Unfortunately, this section will have to be repeated every time the program is run. To begin, open a new graded practice. Click "Customize" in the upper-right corner.
![Graded Practice](/img/gp.png)
Once there, change the verb, tense, and form so that each has only one option selected in the dropdown. The correct answer for the selected options should be the value of `CORRECT` in `conjuguemos.py`. For example, if you select "leer / preterite / yo," `conjuguemos.py` should say `CORRECT = 'leo'`. Select something where the answer doesn't have an accent or &ntilde;, since the program currently doesn't support either. This is coming in a later version.<br>
![Customize](/img/customize.png)<br>
Click "Save settings" and go to the next section. If that's already been completed, skip to [Running the program](#Running-the-program).
## Setting up the program
To set up the program, open `conjuguemos.py` in any text editor. I recommend [Notepad++](https://notepad-plus-plus.org/), but Notepad or TextEdit will work just fine. Looking at the first 12 lines, edit the variables according to the instructions in the file. Don't remove any single-quotes (`'`), as this will cause an error and prevent the program from running.
## Running the program
Open `conjuguemos.py` with a double-click. After the file is open, click on the input box on [Conjuguemos.com](conjuguemos.com). Then, wait for the console window to say `Done.` or for the program to stop typing. Then, record your score using the button in the upper right.
