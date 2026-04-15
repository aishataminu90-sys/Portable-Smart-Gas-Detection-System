import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    while True:
        gas_level = int(input("Enter gas level: "))

        print(f"\nGas Level: {gas_level}")

        # Thresholds
        THRESHOLD_HIGH = 300
        THRESHOLD_MEDIUM = 150

        # Detection logic + buzzer control
        if gas_level > THRESHOLD_HIGH:
            status = " DANGER: Gas Leak Detected!"
            red_led = True
            green_led = False
            GPIO.output(BUZZER_PIN, GPIO.LOW)   # ON

        elif gas_level > THRESHOLD_MEDIUM:
            status = " WARNING: Gas Level Rising"
            red_led = False
            green_led = False
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # OFF

        else:
            status = " Safe Levels"
            red_led = False
            green_led = True
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # OFF

        # Output
        print(status)
        print(f"RED LED: {'ON' if red_led else 'OFF'}")
        print(f"GREEN LED: {'ON' if green_led else 'OFF'}")
        print("-" * 30)

        time.sleep(1)

except ValueError:
    print(" Please enter a valid number")

except KeyboardInterrupt:
    print("\nProgram stopped")

finally:
    GPIO.cleanup()
