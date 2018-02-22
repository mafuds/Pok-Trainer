# -*- coding: utf-8 -*-

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def battle():
    keyboard.press(Key.end)
    keyboard.release(Key.end)

def walk():
    keyboard.press(Key.right)
    time.sleep(0.5)
    keyboard.release(Key.right)
    keyboard.press(Key.left)
    time.sleep(0.5)
    keyboard.release(Key.left)

# Delay
time.sleep(1)

# Fast forward
keyboard.press(Key.space)

while True:
    for x in xrange(0,2):
        walk()
    for x in xrange(0,15):
        battle()
        time.sleep(0.3)
