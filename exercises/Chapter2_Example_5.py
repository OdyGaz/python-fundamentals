def main():
    val  = eval(input("Εισάγετε έναν ακέραιο: "))
    for i in range(val):
        print(i, end="*")
    
    print("Τέλος")

    val  = eval(input("Εισάγετε έναν ακέραιο: "))
    for i in range(1, val):
        print(i, end="*")
    
    print("Τέλος")


main()
