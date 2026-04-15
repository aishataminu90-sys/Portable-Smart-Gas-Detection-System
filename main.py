while True:
    try:
        gas_level = int(input("Enter gas level: "))

        print(f"\nGas Level: {gas_level}")

        # Thresholds
        THRESHOLD_HIGH = 300
        THRESHOLD_MEDIUM = 150

        # Detection logic
        if gas_level > THRESHOLD_HIGH:
            status = "?? DANGER: Gas Leak Detected!"
            red_led = True
            green_led = False

        elif gas_level > THRESHOLD_MEDIUM:
            status = "?? WARNING: Gas Level Rising"
            red_led = False
            green_led = False

        else:
            status = "?? Safe Levels"
            red_led = False
            green_led = True

        # Output results
        print(status)
        print(f"RED LED: {'ON' if red_led else 'OFF'}")
        print(f"GREEN LED: {'ON' if green_led else 'OFF'}")
        print("-" * 30)

        time.sleep(1)

    except ValueError:
        print("? Please enter a valid number")
