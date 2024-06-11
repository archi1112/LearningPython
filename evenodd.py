def main():
    x = int(input("Enter a number"))
    if (EvenOrOdd(x)):
        print("Even")
    else:
        print("Odd")

def EvenOrOdd(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
main()
    