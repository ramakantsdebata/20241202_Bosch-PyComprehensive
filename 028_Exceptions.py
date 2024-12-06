def RegisterStudent(age):
    try:
        age = int(age)
    except ValueError:
        raise TypeError("The Data type is incorrect")
    
    if age < 5:
        raise ValueError("Too small in age")
    elif age > 10:
        raise ValueError("Elder than permitted age group")
    else:
        print("Registered student for the event.")

def div(num, den):
    try:
        res = num/den
    except ZeroDivisionError as ex:
        print("ZeroDivisionError", str(ex))
        raise
    return res

def Main():
    num = 10 #(input("Enter Numerator: "))
    den = 0 #int(input("Enter Denominator: "))

    try:
        res = div(num, den)
        print(res)
    except Exception as ex:
        print("Division operation failed", repr(ex))

    print("All done")



if __name__ == "__main__":
    # Main()

    try:
        RegisterStudent("Three")
    except (ValueError, TypeError) as ex:
        print(f"VALUE/TYPE ERROR --> [{ex!r}]")
    except Exception as ex:
        print(f"EXCEPTION --> [{ex!r}]")

    print("Exiting normally")
