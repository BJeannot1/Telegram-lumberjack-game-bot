from selenium import webdriver
import os
from time import sleep
from PIL import Image
import win32api, win32con
import shutil
import numpy as np

##define a function clicking to wanted coordinates
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#delete old image directory (if any) and creates a neww empty one
if not os.path.exists("im_lmbjk"):
    os.makedirs("im_lmbjk")
else:
    shutil.rmtree(path="im_lmbjk")
    os.makedirs("im_lmbjk")

#readparameters
file_params=np.loadtxt(fname="parametres.txt",
                       dtype=str,
                       delimiter=",",
                       comments="#")
bushColorlimitBLU=int(file_params[0][1])
bushcoordlX=int(file_params[1][1])
bushcoordrX=int(file_params[2][1])
startclickx=int(file_params[3][1])
startclicky=int(file_params[4][1])
startclick=(startclickx,startclicky)
leftclick=(int(file_params[5][1]),int(file_params[6][1]))
rightclick=(int(file_params[7][1]),int(file_params[8][1]))
vert_dist_between_bush=int(file_params[9][1])
secondary_bush_y_coord=int(file_params[10][1])
right_gameover=(int(file_params[11][1]),int(file_params[13][1]))
left_gameover=(int(file_params[12][1]),int(file_params[13][1]))
axe_col_gameover=int(file_params[14][1])

#initialisation
colleft=[255,255,255,255,255,255] #initialisation for the color vector on the left. It describes the level of blue of 6 pixels corresponding to 6 potential branches
colright=[255,255,255,255,255,255] #initialisation for the color vector on the left. It describes the level of blue of 6 pixels corresponding to 6 potential branches


# Open the browser on the webpage of the game
game = webdriver.Firefox()
url = "https://tbot.xyz/lumber/#eyJ1IjoxMTgyMDUxMTQ2LCJuIjoiQmVuemkgSiIsImciOiJMdW1iZXJKYWNrIiwiY2kiOiIzOTc5NTU4MzQ2NjExMDk2MTc3IiwiaSI6IkJBQUFBQVFBQUFCS3EzUkcySjFGSTBsTEhYYyJ9NmUxMzA4ZjVmYTFjMmVhNWVkYTQ5NzEyNzVjYzJlN2I=&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D-D4pwwx_VnDH33gGq6bKWSjcRfgcUMFpmN4_ih_oUfc"
game.get(url)
#Change size of window
game.maximize_window()

#Start game
click(startclick[0], startclick[1])
sleep(1)
#first two inputs
click(leftclick[0], leftclick[1])
click(leftclick[0], leftclick[1])

#following inputs
index = 1
continue_=True
while(continue_):
    sleep(0.00001)
    # Save a picture of the current state of the game
    game.save_screenshot('im_lmbjk/lumberjack' + str(index) + '.png')
    im = Image.open('im_lmbjk/lumberjack' + str(index) + '.png')

    #Locate the Y coordinate of the highest branch. Because of how the game is made if there is no branch at height Y=1 there is necessarily a branch at height Y=secondary_bush_y_coord
    bushcoordY=1
    max_bushes_on_vertical=5
    bushcoordlfirst = (bushcoordlX, bushcoordY)
    bushcoordrfirst = (bushcoordrX, bushcoordY)
    colleft[0] = im.getpixel(bushcoordlfirst)[2]
    colright[0] = im.getpixel(bushcoordrfirst)[2]
    if ((colleft[0]>bushColorlimitBLU) and (colright[0]>bushColorlimitBLU)):
        bushcoordY = secondary_bush_y_coord
        max_bushes_on_vertical=4
    #loop on each potential branch to check if you should cut on the left or the right sindexe
    for i in range(max_bushes_on_vertical, -1, -1):
        colleft[i] = im.getpixel((bushcoordlX, bushcoordY + vert_dist_between_bush * i))[2]
        colright[i] = im.getpixel((bushcoordrX, bushcoordY + vert_dist_between_bush * i))[2]
        if (colleft[i]<bushColorlimitBLU ):
            click(rightclick[0],rightclick[1])
            click(rightclick[0], rightclick[1])
            sleep(0.000001)
        elif (colright[i]<bushColorlimitBLU ):
            click(leftclick[0], leftclick[1])
            click(leftclick[0], leftclick[1])
            sleep(0.000001)
    index =index+1
    #check if game over
    colleft_gameover= im.getpixel(left_gameover)[0]
    colright_gameover=im.getpixel(right_gameover)[0]
    if ((colleft_gameover==axe_col_gameover)or (colright_gameover==axe_col_gameover)):
        continue_=False
    


