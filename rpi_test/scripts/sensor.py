import RPi.GPIO as GPIO
import time

trig=12
echo=16

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)


def loop():
    
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

        if dist < 30 and dist > 4:
            print(f"The distance measured was {dist}")
        else:
            print("Strange distance of {dist} was measured, try again")

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
