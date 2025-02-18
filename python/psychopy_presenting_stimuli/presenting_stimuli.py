from psychopy import visual, event, core # import the bits of PsychoPy we'll need for this walkthrough
import os # import sound package
from helper import load_files

#open a window
win = visual.Window([800,800],color="grey", units='pix', checkTiming=False) 

#add mouse 
mouse = event.Mouse(win = win)

#positions
positions = {"left": (-200,0),"right": (200,0)}

# add rect frame
visual.Rect(win, fillColor = "white", linewWidth = 5, linColor = "black", size = [225,255], pos = positions[pos_key]) for pos_key in positions.keys()

#add text prompt
instruction_text = "click on the bulcasuar"
instruction = visual.TextSim(win, text = instruction_text, pos= (0, -150)

#create images, more universal pull 
image_path_1 = os.path.join(os.getcwd(),"stimuli","images","bulbasaur.png")
image_path_2 = os.path.join(os.getcwd(),"stimuli","images","charmander.png")

image_1 = visual.ImageStim(win,image=image_path_1,size=[200,200],pos=positions["left"])
image_2 = visual.ImageStim(win,image=image_path_2,size=[200,200],pos=positions["right"])

#draw frame
for frame in frame_list:
    frame.draw()

# draw instructions 
instruction.draw()

# draw images
image_1.draw()
image_2.draw()

#show
win.flip()

#check mouse until pressed in one of the pics
while True:
    if mouse.isPressedIn(image_1) or mouse.isPressedIn(image_2):
        response = mouse.getPos()
        print(response)
        break

# checks image
if image_1.cotains(response):


#wait 5 seconds
core.wait(5)

win.close() #close the window
core.quit() #quit out of the program



# add audio