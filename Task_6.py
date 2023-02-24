a = int(input())   
if (len(str(a)) == 6):
    a1 = a // 100000
    a2 = a // 10000 % 10
    a3 = a // 1000 % 100 % 10
    a4 = a // 100 % 1000 % 100 % 10
    a5 = a // 10 % 10000 % 1000 % 100 % 10
    a6 = a % 10
    b1 = (a1 + a2 + a3)
    b2 = (a4 + a5 + a6)
    if (b1 == b2):
        print("yes")
    else:
        print("no")
else:
    print("no")