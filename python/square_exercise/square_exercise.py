import time
import sys
from psychopy import visual,event,core # import the bits of PsychoPy we'll need for this exercise

# win = visual.Window([400,400],color="black", units='pix',checkTiming=False) #open a window
# square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) #create a Rectangle type object with certain parameters
# square.draw() #draw the square to the screen buffer
# win.flip() #make the buffer visible, i.e., show what's been drawn to it
# core.wait(0.5) #pause for half a second (i.e., 500 ms)
# win.close() #close the window -- don't need this if you're running this as a separate file
# core.quit() #quit out of the program -- don't need this if you're running this as a separate file

#exercise 1
win = visual.Window([400,400],color="black", units='pix',checkTiming=False) #open a window
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) #create a Rectangle type object with certain parameters

color_trials = ["blue", "red", "blue", "red", "blue", "red"]
for square_color in color_trials:
    square.color =  square_color
    square.draw()
    win.flip()
    core.wait(1)
    win.flip()
    core.wait(0.05)
    if square.color == "red": # exerise 5
         square.setOri(45)
         core.wait(1)
    else: 
        continue
    space_press = waitKeys(keyList=[" "])
    if space_press:
        win.flip()
