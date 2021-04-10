import tkinter as tk
from time import sleep
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

## Hardware
led = LED(14)

## GUI
win = tk.Tk()
win.title("Morse Blink")
buttonFont = tk.font.Font(family = 'Helvetica', size = 12, weight = "normal")

## Program Functions
def dot():
        led.on()
        sleep(0.25)
        led.off()
        sleep(0.25)

def dash():
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)

def morseBlink():
        entryString = str(entry.get()).lower() #converts the string into lowercase
        for i in range(1, 13):
                if entryString[i] == "a":
                        dot()
                        dash()
                if entryString[i] == "b":
                        dash()
                        dot()
                        dot()
                        dot()
                if entryString[i] == "c":
                        dash()
                        dot()
                        dash()
                        dot()
                if entryString[i] == "d":
                        dash()
                        dot()
                        dot()
                if entryString[i] == "e":
                        dot()
                if entryString[i] == "f":
                        dot()
                        dot()
                        dash()
                        dot()
                if entryString[i] == "g":
                        dash()
                        dash()
                        dot()
                if entryString[i] == "h":
                        dot()
                        dot()
                        dot()
                        dot()
                if entryString[i] == "i":
                        dot()
                        dot()
                if entryString[i] == "j":
                        dot()
                        dash()
                        dash()
                        dash()
                if entryString[i] == "k":
                        dash()
                        dot()
                        dash()
                if entryString[i] == "l":
                        dot()
                        dash()
                        dot()
                        dot()
                if entryString[i] == "m":
                        dash()
                        dash()
                if entryString[i] == "n":
                        dash()
                        dot()
                if entryString[i] == "o":
                        dash()
                        dash()
                        dash()
                if entryString[i] == "p":
                        dot()
                        dash()
                        dash()
                        dot()
                if entryString[i] == "q":
                        dash()
                        dash()
                        dot()
                        dash()
                if entryString[i] == "r":
                        dot()
                        dash()
                        dot()
                if entryString[i] == "s":
                        dot()
                        dot()
                        dot()
                if entryString[i] == "t":
                        dash()
                if entryString[i] == "u":
                        dot()
                        dot()
                        dash()
                if entryString[i] == "v":
                        dot()
                        dot()
                        dot()
                        dash()
                if entryString[i] == "w":
                        dot()
                        dash()
                        dash()
                if entryString[i] == "x":
                        dash()
                        dot()
                        dot()
                        dash()
                if entryString[i] == "y":
                        dash()
                        dot()
                        dash()
                        dash()
                if entryString[i] == "z":
                        dash()
                        dash()
                        dot()
                        dot()


## Widgets

tk.Label(win, text="Enter your message: ").grid(row=0)
entry = tk.Entry(win)
entry.grid(row=0, column=1)
morseButton = tk.Button(win, text = 'Blink in Morse Code', font = buttonFont, command = morseBlink, bg = 'bisque2', height = 1, width = 24).grid(row=3,column=1,sticky=tk.W,pady=4)
