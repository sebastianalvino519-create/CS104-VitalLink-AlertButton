import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Someone pressed the alert button!")
    time.sleep(0.1)
button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)
