def km_to_miles():
    km = float(input("Enter KM : "))
    print("Miles : ",km*0.621371)
    
def c_to_f():
    c = float(input("Enter Celsius : "))
    print("Fahreheit : (c * 9/5 + 32)")
    
def convert_menu():
    print("\n1. KM to Miles")
    print("2. Celsius to Fahrenheit")

    ch = input("Enter choice: ")

    if ch == "1":
        km_to_miles()
    elif ch == "2":
        c_to_f()