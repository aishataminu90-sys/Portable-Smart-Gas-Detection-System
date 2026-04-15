import RPi.GPIO as GPIO
import time

GREEN = 17
YELLOW = 27
RED = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

try:
    while True:
        print("GREEN ON")
        GPIO.output(GREEN, True)
        GPIO.output(YELLOW, False)
        GPIO.output(RED, False)
        time.sleep(2)

        print("YELLOW ON")
        GPIO.output(GREEN, False)
        GPIO.output(YELLOW, True)
        GPIO.output(RED, False)
        time.sleep(2)

        print("RED ON")
        GPIO.output(GREEN, False)
        GPIO.output(YELLOW, False)
        GPIO.output(RED, True)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
