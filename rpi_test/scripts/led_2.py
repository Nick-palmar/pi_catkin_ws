#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# ROS imports
from rpi_test.srv import ledControl, ledControlResponse
import rospy

led_pin = 21
# set up code
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT)

def loop():
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)

def stop():
    GPIO.cleanup()

def handle_led_control(req):


if __name__ == "__main__":
    # print("Starting led control node")
    setup()

    try:
        led_control_server()
    except KeyboardInterrupt:
        stop()
