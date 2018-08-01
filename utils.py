def inputNumber(message):
    """
    Asks the user for a enter a number based on the message being asked
    :param message: What message is asked to the user
    :return: number user entered
    """
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Oops. Not a valid input. Must be number.")
            continue
        else:
            return userInput

def inputNumberOrReturn(message):
    """
       Asks the user for a enter a number based on the message being asked
       :param message: What message is asked to the user
       :return: number user entered
    """
    guess = input(message)
    if not guess:
        return 0

    try:
        # CONVERT GUESS INTO A NUMBER
        guess = int(guess)
    except ValueError:
        print("Oops. We need a number or return which defaults to 0")
    else:
        return guess