from flask import Flask, render_template, request, redirect
from datetime import date
import sys
import board
import neopixel
import random
from random import randrange
import time
pixels = neopixel.NeoPixel(board.D18, 60)

#Warn to run as root / sudo
print("YOU NEED TO RUN THIS AS SUDO USER FOR IT TO WORK!")
app = Flask(__name__)

#Set Colour Functions
def LED_green():
    pixels.fill((0, 255, 0))
def LED_blue():
    pixels.fill((0,0,255))
def LED_red():
    pixels.fill((255,0,0))
def LED_random():
    pixels.fill((randrange(255), randrange(255), randrange(255)))
   


@app.route('/') # default homepage 
def home():
    return 'Try going somewhere else'

@app.route('/admin_control')
def index():
    return render_template('index.html')

@app.route('/red', methods=['POST'])
def move_forward():
    #run some python code
    print("Lets Go Red!", file=sys.stderr)
    LED_red()
    return ('', 204) # empty response


@app.route('/blue', methods=['POST'])
def turn_blue():
    #run some python code
    print("Lets Go Blue", file=sys.stderr)
    LED_blue()
    return ('', 204) # empty response


@app.route('/green', methods=['POST'])
def turn_green():
    #run some python code
    print("Lets Go Green!", file=sys.stderr)
    LED_green()
    return ('', 204) # empty response


@app.route('/rainbow', methods=['POST'])
def turn_rainbow():
    #run some python code
    print("Lets Go Rainbow!", file=sys.stderr)

    return ('', 204) # empty response


@app.route('/random', methods=['POST'])
def turn_random():
    #run some python code
    print("Lets Go Random!", file=sys.stderr)
    for i in range(20):
        LED_random()
        time.sleep(0.2)
        LED_green()
        
    

    return ('', 204) # empty response

@app.route('/animation', methods=['POST'])
def turn_animated():
    #run some python code
    print("Lets Go Animation!", file=sys.stderr)

    return ('', 204) # empty response




if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.run(debug=True)
