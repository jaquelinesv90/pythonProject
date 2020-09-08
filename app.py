command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("car is already stoped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("start - to start the car")
    elif command == "quit":
        break
    else:
        print("sorry, i don't understand")