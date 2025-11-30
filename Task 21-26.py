print("Task 21")
def greeting(name):
    print(f"What's up {name}???")
user_name=input("Enter your name sir: ")
greeting(user_name)
print("")
print("Task 22")
def blabla(name1):
    return f"HELLO {name1}!!!"
user_name1=input("C-can you...emm...enter your name, pls: ")
print(blabla(user_name1))
print("")
print("Task 23")
def numbers(num1,num2):
    return num1 + num2
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(f"The sum of your numbers is  {numbers(num1,num2)}")
print("")
print("Task 24")
def hi(input_name):
    return f"Hi {input_name}!"
name2=input("Enter your name pls: ")
name3=input("Enter your second name pls: ")
print(hi(name2))
print(hi(name3))
print()
print("Task 25")
def mean_for_numbers(numa,numb,numc):
    return (numa+numb+numc)/3
numa=float(input("Enter your number one: "))
numb=float(input("Enter your number two: "))
numc=float(input("Enter your number three: "))
print(f"The mean of your three numbers is {mean_for_numbers(numa,numb,numc)}")
print()
print("Task 26")
my_flag= True
while my_flag:
    namebb=input("Say my name: ")
    if namebb == "Heisenberg":
        my_flag= False
        print("You're goddamn right!")



