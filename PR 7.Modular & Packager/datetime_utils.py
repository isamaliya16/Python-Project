from datetime import datetime
import time

def show_datetime():
    print("Current Date & time : ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
def date_difference(): 
    d1 = input("Enter first date (YYYY-MM-DD): ")
    d2 = input("Enter second date (YYYY-MM-DD): ")
    diff = datetime.strptime(d2,"%Y-%m-%d") - datetime.strptime(d1,"%Y-%m-%d")
    print("Difference : ",diff.days,"days")
    
def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    print("Elapsed:", time.time() - start, "seconds")
    
def countdown():
    sec = int(input("Enter seconds :"))
    while sec > 0 :
        print(sec)
        time.sleep(1) 
        sec -=  1
        print("Time upi")
        
def show_datetime_menu():
    print("\n1. Show Current Date & Time")
    print("2. Date Difference")
    print("3. Stopwatch")
    print("4. Countdown Timer")

    ch = input("Enter choice: ")

    if ch == "1":
        show_datetime()
    elif ch == "2":
        date_difference()
    elif ch == "3":
        stopwatch()
    elif ch == "4":
        countdown()
        