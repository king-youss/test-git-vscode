num = 67

flag = False
if num == 1:
    print(num, "n'est pas un nombre premier")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "n'est pas un nombre premier")
    else:
        print(num, "est un nombre premier")