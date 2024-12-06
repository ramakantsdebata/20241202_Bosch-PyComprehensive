class InvalidAgeError(ValueError):
    def __init__(self, message, code) -> None:
        self. message = message
        self.code = code

class CustomError(Exception):
    def __init__(self, message, code) -> None:
        self. message = message
        self.code = code


def RegisterStudent(age):
    if age < 0:
        raise InvalidAgeError(f"[{age}] --> That is an invalid age", 2)
    elif age < 5 or age > 10:
        raise InvalidAgeError(f"[{age}] --> Only children from 5-10 can register for this event", 1)
    else:
        print("Registered student for the event.")


def Test1():
    try:
        RegisterStudent(-1)
    except InvalidAgeError as ex:
        print(f"{ex!r}")
    except CustomError as ex:
        print(f"{ex!r}")

    try:
        RegisterStudent(3)
    except InvalidAgeError as ex:
        print(f"{ex!r}")
    except CustomError as ex:
        print(f"{ex!r}")

    try:
        RegisterStudent(11)
    except InvalidAgeError as ex:
        print(f"{ex!r}")
    except CustomError as ex:
        print(f"{ex!r}")

    try:
        RegisterStudent(7)
    except InvalidAgeError as ex:
        print(f"{ex!r}")
    except CustomError as ex:
        print(f"{ex!r}")


def Test2():
    # with open("file.txt", "w") as file:
    #     file.write("Some text")

    # try:
    #     file = open("file.txt", "w")
    #     # File IO
    #     # file.close()
    # except Exception as ex:
    #     print(f"{ex!r}")
    #     # file.close()
    # finally:
    #     file.close()


    try:
        with open("file.txt", "w") as file:
            file.write("Some text")
    except Exception as ex:
        print(f"{ex!r}")
    finally:
        # Release other resource and cleanup
        pass

    print("Back to normal")



if __name__ == "__main__":
    Test2()