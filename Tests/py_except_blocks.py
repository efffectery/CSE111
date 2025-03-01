# python

def recive_age():
    done = False
    while not done:
        try:
            age = int(input("Please input yout age (0-125) "))
            if age >= 0 and age <= 125:
                done = True
            else:
                print("Please input a valid age")
        except ValueError as value_error:
            print("Try again make sure you enter a whole number between 0 and 125")
        except KeyboardInterrupt:
            print(f" lol nice try ")
            raise Exception("fine you can leave")
    return age

def main():
    try:

        age = recive_age()
        print(f"Your age is: {age}")
    except Exception as exception:
        print(f"Error {exception}")


if __name__ == "__main__":
    main()