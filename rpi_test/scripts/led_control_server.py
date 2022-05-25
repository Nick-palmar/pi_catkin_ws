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

def led_control_server():
    rospy.init_node('led_control_server')
    serv = rospy.Service('led_control', ledControl, handle_led_control)
    rospy.spin()

def stop():
    GPIO.cleanup()

def handle_led_control(req):
    try:
        if req.turn_on:
            GPIO.output(led_pin, GPIO.HIGH)
            msg = 'LED on'
        else:
            GPIO.output(led_pin, GPIO.LOW)
            msg = 'LED off'
        success = True
    except Exception as err:
        success = False
        msg = err

    return {'success': success, 'msg': msg}
        

if __name__ == "__main__":
    # print("Starting led control node")
    setup()

    try:
        led_control_server()
    except KeyboardInterrupt:
        stop()
