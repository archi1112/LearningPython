# match and switcher are both the same as switch 

def SwitchProg(arg):
    switcher = {
        0: "case 0",
        1:"case 1",
        2:"case 2"
    }
    return switcher.get(arg,"nothing")

def matchProg(arg):
    match arg:
        case 0 : print("case 0"),
        case 1 : print("case 1"),
        case 2 : print("case 2")

def main():
    arg=1
    print(SwitchProg(arg))
    matchProg(arg)

main()