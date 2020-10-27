# Google Meet bot! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">

A Basic Google Meet bot that can attend all of your classes :)

## DISCLAIMER
This bot is created for educational purposes only, I am not responsible for the misuse of this product.

## REQUIREMENTS
1. pip install selenium <br /> 
2. pip install keyboard <br />
3. Chrome Driver (add the exe in same folder as of the bot): https://chromedriver.chromium.org/home
 
## Features:
1. I added a basic menu if you want to make an exe and send it to your friend.<br />
2. File saving/loading system added:<br />
All the values you input in the menu will be saved in a text file and will be loaded on your next start.<br />
3. Only one google meet link added but you can modify the code and add according to your preference.<br />
4. 3 Lectures added only if you have more lectures just modify according to your preference.<br />
5. Mark your attendance in chat box.
6. I have added the exe version aswell so you can use it and see the working of the bot.
7. Auto Leaves the class after its ended (you need to set the time)

## Note (Installation):
First Install the files in requirements
Then Simply open CMD and type: python filename.py to run it.

## FAQ: 
The bot is not working properly after GMAIL Login?<br />
Make sure you have both Mic and Webcam or you can simply remove the one set of lines one time:
> keyboard.press_and_release('tab, tab')<br /> 
> keyboard.press_and_release('enter, enter')

Why don't you simply use the experimental features in Chrome?<br />
As of now the features are bugged IDK why as I have tested the same thing on Mozilla driver and it  worked fine.

How can I add more Urls?<br />
The Simplest approach is to use fstring and take 5 input (if you have 5 different URLS) from user and the save em in TXT file, Read the code you will get it.


## Upcoming Features:
1. Recording the whole lecture<br />
2. Image to Text (get all your notes extracted from the image to text)

## Have a nice day :)
