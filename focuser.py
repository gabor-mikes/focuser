#!/usr/bin/python3

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from tkinter import *
#from tkinter.ttk import *

import sys

Position = 0
Steps = 6
Microsteps = 50
Verbose = False
   
def step(steps):
    global Position
    global Microsteps
    m = MotorKit()
    if(steps > 0):
        for i in range(int(steps)):
            for j in range(Microsteps):
                m.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
            Position += Microsteps
            ivPosition.set(Position)
            app.update()
    else:
        for i in range(int(-steps)):
            for j in range(Microsteps):
                m.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
            Position -= Microsteps
            ivPosition.set(Position)
            app.update()
    m.stepper1.release()
    svStatus.set("At position " + str(Position) + " steps")

def step_p1():
    global Steps
    step(Steps)

def step_p2():
    global Steps
    step(Steps*3)

def step_p3():
    global Steps
    step(Steps*9)
   
def step_m1():
    global Steps
    step(-Steps)
   
def step_m2():
    global Steps
    step(-Steps*3)
   
def step_m3():
    global Steps
    step(-Steps*9)
   
def chang_position(value):
    global Position
    global Microsteps
    step((int(value) - Position)/Microsteps)
        
def goto_position():
    global Position
    global Microsteps
    step((ivGoto.get() - Position)/Microsteps)
   
def zero():
    global Position
    Position = 0
    ivPosition.set(Position)
    svStatus.set("At position " + str(Position) + " steps")
   
def set_steps():
    global Steps
    global Verbose
    Steps = ivSteps.get()
    if(Verbose):
        print("Set steps to " + str(Steps))

def set_microsteps():
    global Microsteps
    global Verbose
    Microsteps = ivMicrosteps.get()
    if(Verbose):
        print("Set microsteps to " + str(Microsteps))

sFg = "#cccccc"
sBg = "#555555"
sBg2 = "#888888"
sFg2 = "#111111"

app = Tk()
app.title("Adafruit Motor Hat Focuser")
#app.configure(bg=sB)
#app.tk_setPalette(background='DimGray', foreground='DarkOrange2', activeBackground='Gray', activeForeground='DarkOrange1')
app.tk_setPalette(background='DimGray', foreground='GhostWhite', activeBackground='Gray', activeForeground='White')

# Steps
svLbl1 = StringVar()
svLbl1.set("Steps")
Label(app, textvariable=svLbl1).grid(row=1, column=0, columnspan=1)

#Progressbar(app)

ivSteps = IntVar()
ivSteps.set(6)
Spinbox(app, from_=1, to=15, textvariable=ivSteps, command=set_steps, width=5).grid(row=1, column=1, columnspan=2)

# Microsteps
lbl2 = StringVar()
lbl2.set("Microsteps")
Label(app, textvariable=lbl2, justify=RIGHT).grid(row=1, column=4, columnspan=2)
ivMicrosteps = IntVar()
Spinbox(app, values=(50,75,100,10,25), textvariable=ivMicrosteps, wrap=True, command=set_microsteps, width=5).grid(row=1, column=6, columnspan=2)

# Go to
lbl3 = StringVar()
lbl3.set("Position")
Label(app, textvariable=lbl3).grid(row=1, column=8, columnspan=2)

ivGoto = IntVar()
ivGoto.set(0)
Entry(app, textvariable=ivGoto, width=8).grid(row=1, column=10, columnspan=2)
Button(app, command=goto_position, text="Go").grid(row=1, column=12, columnspan=1)

svStatus = StringVar()
svStatus.set("At position 0 steps")
Label(app, textvariable=svStatus).grid(row=1, column=13, columnspan=5)

#zero
Button(app, command=zero, text="Zero").grid(row=2, column=0)

#silder
ivPosition = IntVar()
Scale(app, command=chang_position, variable=ivPosition, from_=-30000, to=30000, width=30, length=740, orient=HORIZONTAL).grid(row=3, column=0, columnspan=18)

# Buttons
b_r = 4
Button(app, command=step_p3, width=12, text=">>>").grid(row=b_r,column=15, columnspan=3)
Button(app, command=step_p2, width=12, text=">>").grid(row=b_r,column=12, columnspan=3)
Button(app, command=step_p1, width=12, text=">").grid(row=b_r,column=9, columnspan=3)
Button(app, command=step_m1, width=12, text="<").grid(row=b_r,column=6, columnspan=3)
Button(app, command=step_m2, width=12, text="<<").grid(row=b_r,column=3, columnspan=3)
Button(app, command=step_m3, width=12, text="<<<").grid(row=b_r,column=0, columnspan=3)
app.mainloop()
