while True:
    try:
        number = int(input("What is your number?\n"))
        print(18/number)
        break

    except ValueError:
        print("Make sure and enter number:")

    except ZeroDivisionError:
        print("Don't pick zero")



