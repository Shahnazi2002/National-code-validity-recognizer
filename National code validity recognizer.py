n = input("Enter the national code: ")

digits = list(map(int, f"{n}"))
length = len(digits) == 10

if length == True:
    validity = (digits[0]*10) + (digits[1]*9) + (digits[2]*8)
    + (digits[3]*7) + (digits[4]*6) + (digits[5]*5)
    + (digits[6]*4) + (digits[7]*3) + (digits[8]*2)
    remainder = validity % 11
    if remainder == 0:
        if digits[9] == 0:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 1 or remainder == 10:
        if digits[9] == 1:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 2:
        if digits[9] == 9:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 3:
        if digits[9] == 8:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 4:
        if digits[9] == 7:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 5:
        if digits[9] == 6:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 6:
        if digits[9] == 5:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 7:
        if digits[9] == 4:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 8:
        if digits[9] == 3:
            print("Vaild!")
        else:
            print("Not Vaild!")
    elif remainder == 9:
        if digits[9] == 2:
            print("Vaild!")
        else:
            print("Not Vaild!")
else:
    print("Not Vaild!")
