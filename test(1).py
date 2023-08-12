
from gpiozero import Servo
from time import sleep
import random

animals=["cat","dog","dolphin","horse","tiger"]
 

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
              
        