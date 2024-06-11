# main function
def main():
    print("In main")
    greeting()
    greet_with_params("yukta")


# function
def greeting():
    print("hello")

# function with parameters
def greet_with_params(name):
    print(f"hello {name}")


# calling main
main()