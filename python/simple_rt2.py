from psychopy import visual, event, core # import the bits of PsychoPy we'll need for this walkthrough

#open a window
win = visual.Window([600,600],color="grey", units='pix', checkTiming=False) 

#create a blue circle
circle = visual.Circle(win,lineColor="grey",fillColor="blue",size=[100,100])

#adding intructions 
instruction_text = "press the first letter of the circle's color"
instruction = visual.TextStim(win, text = instruction_text, pos = (0, -100))

# create a list of colors
color_list = ["blue", "orange", "purple", "red"]

for current_color in color_list:
    circle.color = current_current
    circle.draw()
    instruction.draw()
    win_flip()

    key_pressed = event.waitKeys(keyList=["b", "o", "p", "r"])
if key_pressed:
    print(key_pressed)
win.flip()
core.wait(1.0)


#show the blue circle
#first, draw the blue circle to the back buffer of the window
#this means that the blue circle won't be displayed right away
circle.draw()
#then "flip" the window to show what you just drew
win.flip()

#using event, specifies for type of key pressed
key_pressed = event.waitKeys(keyList=["b", "o"])
if key_pressed:
    print(key_pressed)
    win.flip()  # doesn't have to be embedded

core.wait(1.0)

#wait for 1 second
#adding orange circle
circle.color = "orange"
circle.draw()
win.flip()

key_pressed = event.waitKeys(keyList=["b", "o"])
if key_pressed:
    print(key_pressed)
    win.flip()

#wait 2 seconds
core.wait(2.0)

win.close() #close the window
core.quit() #quit out of the program