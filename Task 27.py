print("Task 27")
my_flag=True

password=input("Enter your password: ")

while my_flag:
    password_again=input("Enter your password again: ")
    if password_again==password:
        print("Your password matches and account created successfully!")
        my_flag=False
    else:
        print("They're not same.")
    
        