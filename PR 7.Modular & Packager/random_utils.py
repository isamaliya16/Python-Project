import random 
import string 

def random_number() :
    print("Random Number (1-100):",random.randint(1,100))
    
def random_list():
    print("Random List : ",random.sample(range(1,50),5))
    
def password_generator():
    size = int(input("Enter the password length : "))
    char = string.ascii_letters + string.digits + string.punctuation
    pwd = ""
    
    for i in range(size):
        pwd = pwd + random.choice(char)
    print("Generated Password : ",pwd)
    
def otp_generator():
    print("otp: ",random.randint(100000,999999))

def show_random_menu():
    print("\n1. Random Number")
    print("2. Random List")
    print("3. Password Generator")
    print("4. OTP Generator")


    ch = input("Enter choice: ")
    if ch == "1":
        random_number()
    elif ch == "2":
        random_list()
    elif ch == "3":
        password_generator()
    elif ch == "4":
        otp_generator()
 