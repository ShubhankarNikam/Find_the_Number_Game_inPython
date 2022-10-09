import random
s=random.randint(1,100)
no=int(input("Enter Your Number: "))
while(no!=s):
    if no>s:
        print("Your number is greater than Hidden Number")
        no=int(input("Enter Your Number Again: "))

    elif no<s:
        print("Your number is less than Hidden Number")
        no=int(input("Enter Your Number Again: "))
    else: 
        break

if no==s:
    print("Congratulations, You found hidden number correctly!!!")
    

    