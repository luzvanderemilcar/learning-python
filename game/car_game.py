# Car game
command = ""
car_current_status = ""
stopped_status = "stopped"
started_status = "started"
while True:
    command = input("> ").lower()
    if command == "start":
        if car_current_status == started_status:
            print("Car has been already started")
        else:
            print("Started... Ready to go !")
            car_current_status = started_status
    elif command == "stop":
        if car_current_status == stopped_status:
            print("Car has been already stopped")
        elif car_current_status != started_status:
            print("Car has not yet started")
        else:
            print("Car has been stopped")
            car_current_status = stopped_status
    elif command == "quit":
        print("See you next time")
        break
    elif command == "help":
        print('''
        \rCommand list
        \rstart - to start the car
        \rstop - to stop the car
        \rquit - to quit
        \rhelp - to get help
        ''')
    else:
        print("Opps ! Enter a valid command")
