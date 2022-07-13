### This repositories presents a bot I made that plays the telgram lumberjack game. To the best of my knowledge, this is the best bot on the internet for this game (Max score : 1050).

# **I.	Quick description of the game**

In this game, the user plays as a lumberjack cutting an infinitely tall tree. The goal is to chop the highest possible amount of wood pieces before you run out of time, by choping on either the left or right side of the tree. However, while choping, the lumberjack must also dodge the failing tree branches, by standing on the opposite side of the tree. Touching a branch leads to a game over. An image from the game is shown below.

![alt text](https://github.com/BJeannot1/Telegram-lumberjack-game-bot/blob/master/illustration.png?raw=true)

# **II.	Bot playing the game**
  ## 1. Principle
The bot screens the color of specific pixels on each side of the tree, and uses these information in order to determine on what side of the tree to chop. It uses the following python libraries :
-selenium, win32api and win32 con, for automation purposes
-numpy, for reading the file of parameters
-pyautoguy, for saving images of the screen and analyzing pixels color
-shutil, for deleting the folder that stores all the tmporary images created when running the code

The bot's performance compared to other bots on the internet comes from the fact I use a single image to decide about the next 5 to 6 moves, by screening different pixels at the same time, while other bots usually  
  ## 2. Limitations
-This is a bot working on Windows.
-You need Firefox installed
-The default parameters are adapted for a resolution of 1920*1080.


  ## 1.Video of the bot
