import time

print("?? Portable Smart Gas Detection System Starting...")

THRESHOLD_HIGH = 300
THRESHOLD_MEDIUM = 150

while True:
    try:
        gas_level = int(input("Enter gas level: "))

        print(f"Gas Level: {gas_level}")

        if gas_level > THRESHOLD_HIGH:
            print("?? DANGER: Gas Leak Detected!")
        elif gas_level > THRESHOLD_MEDIUM:
            print("?? WARNING: Gas Level Rising")
        else:
            print("?? Safe Levels")

        print("-" * 30)
        time.sleep(1)

    except ValueError:
        print("? Please enter a valid number")
