__all__ = ["greet", "greet_name", "greet_interactive"]

def greet():
    print("Hi there")

def greet_name(name):
    greeting = "Hello"
    final_str = prep_greeting(greeting, name)
    print(final_str)

def prep_greeting(greeting, name):
    return greeting + " " + name + "!!"

def greet_interactive():
    greeting = "Hello"
    name = input("Enter your name: ")
    final_str = prep_greeting(greeting, name)
    print(final_str)

def Test1():
    greet()
    greet_name("Manish")
    greet_interactive()

def Test2():
    """Smoke test"""
    greet()
    print(prep_greeting("Hey", "Tom"))

if __name__ == "__main__":
    Test2()