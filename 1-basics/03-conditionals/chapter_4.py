# nested if

device_status = "active"

temperature = 38

if device_status == "active":
    if temperature > 35:
        print("high Temperature Alert!")
    else:
        print("Normal Temperature")
else:
    print("The  device is offline")