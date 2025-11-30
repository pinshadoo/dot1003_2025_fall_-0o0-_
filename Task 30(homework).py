my_flag=True
totalnumber=0
even=0
odd=0
number=0
print("dumb calculator v0.1 if you want to exit, enter 0")
while my_flag:
    number1=int(input("please enter a number: "))
    if number1==0:
        my_flag=False
        mean=number/totalnumber
        print(f"Total Number:{totalnumber}")
        print(f"Sum:{number}")
        print(f"Mean:{mean}")
        print(f"Odd:{odd}  Even: {even}")
    else:
        number=number1+number
        totalnumber=totalnumber + 1
        if number1%2==0:
            even=even + 1
        else:
            odd=odd +1