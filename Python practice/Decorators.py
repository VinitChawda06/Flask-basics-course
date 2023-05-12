def Greet(func):
    # print("Inside greet")

    def One_more_greet():
        print("Heyy Good morning")

        func()

        print("Bbye time to leave")

    return One_more_greet

@Greet
def hello():
    print("My name is ...")

# hello = Greet(hello)
# ^^^^^ ^ ^^^^^^^^^^^^ this entire assigning is done using decorator before the function
hello()