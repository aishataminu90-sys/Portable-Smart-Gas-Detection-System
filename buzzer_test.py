import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("Testing buzzer module...")

try:
    while True:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)  # OFF for some modules
        print("OFF")
        time.sleep(1)

        GPIO.output(BUZZER_PIN, GPIO.LOW)   # ON for some modules
        print("ON")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
