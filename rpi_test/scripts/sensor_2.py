#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# ros imports
import rospy
from rpi_test.srv import ledControl

trig=12
echo=16

CRITICAL_DIST = 15

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def call_led_control(dist):
    rospy.wait_for_service('led_control')
    try:
        led_control = rospy.ServiceProxy('led_control', ledControl)
        if dist <= CRITICAL_DIST:
            resp = led_control(True)
        else:
            resp = led_control(False)
        return (resp.success, resp.msg)
    except rospy.ServiceException as e:
        return (f"Service call failed: {e}")

def loop():
    GPIO.output(trig, False)
    print("Calibrating")
    time.sleep(2)
    
    while True:
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        # TODO: create an interrupt for this process instead
        while GPIO.input(echo)==0:
            start = time.time()
        while GPIO.input(echo)==1:
            end = time.time()

        pulse_duration = end-start
        dist = pulse_duration * 17150
        dist = round(dist+1.15, 2)

        # create the client call to the led control server
        call_led_control(dist)

        time.sleep(2)

def stop():
    GPIO.cleanup()

if __name__ == "__main__":
    print("Starting sensor.py")
    setup()

    try:
        loop()
    except:
        stop()
