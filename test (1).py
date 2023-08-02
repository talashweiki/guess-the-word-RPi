
from gpiozero import Servo
from time import sleep
import random

words=["cat","dog","dolphin","horse","tiger"]

servo=Servo(18)

 
while True:
    servo.mid()
    r=random.choice(words)
    print(words)
    us=input("Guess the animal: ")
    if r==us:
        print("Excellent")
        servo.max()
        sleep(2)
    elif r!=us:
        print("Try again")
        servo.min()
        sleep(2)
              
            










'''
from gpiozero import Servo
from time import sleep

servo=Servo(18)
while True:
    servo.mid()
    print("mid")
    sleep(1)
    servo.max()
    print("Max")
    sleep(1)
    servo.min()
    print("Min")
    sleep(1)
        
'''