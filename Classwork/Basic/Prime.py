for number in range(3,100):
    flag=0

    for i in range(2,number):
        if number%1==0:
            flag=1
            break

    if flag==0:
     print(number)
