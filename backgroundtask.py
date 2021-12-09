import time 
import board
import neopixel
import random
from random import randrange
pixels = neopixel.NeoPixel(board.D18, 60)

def LED_random():
    pixels.fill((randrange(255), randrange(255), randrange(255)))

def LED_green():
    pixels.fill((0, 255, 0))
def LED_blue():
    pixels.fill((0,0,255))
def LED_red():
    pixels.fill((255,0,0))

def background_task ():
    delay = 10
    time.sleep(delay)
    print("FLASHING LIGHTS")
    for i in range(20):
        LED_random()
        time.sleep(0.2)
        LED_green()

    delay = 4
    time.sleep(delay)


    print("Task Complete")
