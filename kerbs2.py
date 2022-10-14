import random
from tkinter import *

def generate():
    
    nums = []
    hexnums = []

    for i in range (0,6): # generates 6 random numbers (0-255), then converts to hex and removes leading 0x
        rand = random.randint(0, 255)
        nums.append(rand)
        hexnums.append(hex(nums[i]).split("x")[-1])
        if len(hexnums[i]) == 1: # makes sure all hex numbers are two digit
             hexnums[i] = hexnums[i] + '0'

    # creates 2 hex colour codes as strings from these numbers
    col1 = "#"+hexnums[0]+hexnums[1]+hexnums[2]
    col2 = "#"+hexnums[3]+hexnums[4]+hexnums[5]

    # prints the 2 colour codes
    print(col1)
    print(col2)
        
    # tkinter bullshit
    # adds rectangles of the generated colour above the kerb image

    #input("\nEnter to run again\n")
    canvas.itemconfig(leftrect, fill=col1)
    canvas.itemconfig(rightrect, fill=col2)
    label2.config(text = col2)
    label3.config(text = col1)


def generateleft():

    nums =[]
    hexnums = []

    for i in range (0,3):
        rand = random.randint(0, 255)
        nums.append(rand)
        hexnums.append(hex(nums[i]).split("x")[-1])
        if len(hexnums[i]) == 1: # makes sure all hex numbers are two digit
             hexnums[i] = hexnums[i] + '0'
        
    col = "#"+hexnums[0]+hexnums[1]+hexnums[2]
    canvas.itemconfig(leftrect, fill=col)
    label3.config(text = col)

def generateright():

    nums =[]
    hexnums = []

    for i in range (0,3):
        rand = random.randint(0, 255)
        nums.append(rand)
        hexnums.append(hex(nums[i]).split("x")[-1])
        if len(hexnums[i]) == 1: # makes sure all hex numbers are two digit
             hexnums[i] = hexnums[i] + '0'
        
    col = "#"+hexnums[0]+hexnums[1]+hexnums[2]
    canvas.itemconfig(rightrect, fill=col)
    label2.config(text = col)


win1 = Tk()
win1.geometry('800x260')
canvas = Canvas(height=260, width=800,)
bg = PhotoImage(file = 'bitmap.png')
canvas.create_image(0, 0, image = bg, anchor = 'nw')
leftrect = canvas.create_rectangle(215,92,340,155,outline ="black",fill = 'red',width = 0)
rightrect = canvas.create_rectangle(460,92,590,155,outline ="black",fill = 'red',width = 0)
canvas.pack()
win1.title('Colours')

button = Button(win1, text="Change Both", font=('Helvectica 11'),
command = lambda: generate())
button.place(relx=.5, rely=.75, anchor=CENTER)


button2 = Button(win1, text="Change Right", font=('Helvectica 11'),
command = lambda: generateright())
button2.place(relx=.75, rely=.75, anchor=CENTER)
label2 = Label(canvas, text = '')
label2.place(relx=.65, rely=.25, anchor=CENTER)

button3 = Button(win1, text="Change Left", font=('Helvectica 11'),
command = lambda: generateleft())
button3.place(relx=.25, rely=.75, anchor=CENTER)
label3 = Label(canvas, text = '')
label3.place(relx=.35, rely=.25, anchor=CENTER)

win1.mainloop()

generate()
