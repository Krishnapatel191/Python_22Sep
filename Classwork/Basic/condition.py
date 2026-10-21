cont = 'y'
while cont=='y':
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    choice = input("enter opration to b perform : ")

    match(choice):
        case '+': print("addtion is :",a+b)
        case '-': print("substraction is :",a-b)
        case '*': print("multiplcation is :",a*b)
        case '/': print("division is :",a/b)
        case _ : print("invalid operation")
    
    cont = input("do you want to continue? press y or n :")