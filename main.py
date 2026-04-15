print("Portable Smart Gas Detection System Starting...")

while True:
    gas_level = int(input("Enter gas level: "))

    if gas_level > 300:
        print("?? Gas Leak Detected!")
    elif gas_level > 150:
        print("?? Warning: Gas Level Rising")
    else:
        print("? Safe Levels")
