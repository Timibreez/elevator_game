import time


def play_game():
    items = []
    intro()
    ride_elevator(items)


def printt(message):
    print(message)
    time.sleep(1)


def first_floor(items):
    printt("You push the button for the first floor.")
    printt("After a few moments, you find yourself in the lobby.")
    if "ID card" in items:
        printt("The clerk greets you, but she has already given you your"
               "ID card, so there is nothing more to do here now.")
    else:
        printt("The clerk greets you and gives you your ID card.")
        items.append("ID card")
    ride_elevator(items)


def second_floor(items):
    printt("You push the button for the second floor.")
    printt("After a few moments, "
           "you find yourself in the human resources department.")
    if "employee handbook" in items:
        printt("The HR folks are busy at their desks."
               "There doesn't seem to be much to do here.")
    else:
        printt("The head of HR greets you.")
        if "ID card" in items:
            printt("He looks at your ID card and "
                   "then gives you a copy of the employee handbook.")
            items.append("employee handbook")
        else:
            printt("He has something for you,"
                   " but says he can't give it to you until "
                   "you go get your ID card.")
        ride_elevator(items)


def third_floor(items):
    printt("You push the button for the third floor.")
    printt("After a few moments, you find "
           "yourself in the engineering department.")
    if "ID card" in items:
        printt("You use your ID card to open the door.")
        printt("Your program manager greets you and "
               "tells you that you need to have a copy"
               "of the employee handbook in order to start work.")

        if "employee handbook" in items:
            printt("Fortunately, you got that from HR!"
                   "Congratulatons! You are ready to "
                   "start your new job as vice president of engineering!")

        else:
            printt("They scowl when they see that you don't "
                   "have it, and send you back to the elevator.")
            ride_elevator(items)

    else:
        printt("Unfortunately, the door is locked and you can't get in.")
        printt("It looks like you need some "
               "kind of key card to open the door.")
        printt("You head back to the elevator.")
        ride_elevator(items)


def intro():
    printt("You have just arrived at your new job!")
    printt("You are in the elevator.")


def ride_elevator(items):
    response = int(input("""Please enter the number for
        the floor you would like to visit:
        1. Lobby
        2. Human resources
        3. Engineering department \n
        """))

    if response == 1:
        first_floor(items)
    if response == 2:
        second_floor(items)
    if response == 3:
        third_floor(items)


play_game()
