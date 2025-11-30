print("Task 28")
number=int(input("Pls enter a number here: "))
my_flag=True
while my_flag:
    print(number)
    number = number-1
    if number == 0:
        print("KABOOOM!!!")
        my_flag = False