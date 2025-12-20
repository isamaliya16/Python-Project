import datetime_utils
import math_utils
import random_utils 
import uuid_utils
from mypackage import file_ops, convert_utils
def explore_module():
    module_nm = input("Enter module nm to explore (e.g., math,datatime)")
    try : 
        module = __import__(module_nm)
        print(dir(module)) 
    except:
        print("Module not  found.")
        
def main_menu():
    while True:
        print("\n=== Multi Utility Toolkit ===")
        print("1. Datetime & Time Utilities")
        print("2. Math Utilities")
        print("3. Random Utilities")
        print("4. UUID Generator")
        print("5. File Operations (Custom Module)")
        print("6. Unit Conversion (Custom Module)")
        print("7. Explore Module (dir)")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            datetime_utils.show_datetime_menu()
        elif choice == "2":
            math_utils.show_math_menu()
        elif choice == "3":
            random_utils.show_random_menu()
        elif choice == "4":
            uuid_utils.generate_uuid()
        elif choice == "5": 
            file_ops.file_menu()
        elif choice == "6":
            convert_utils.convert_menu()
        elif choice == "7":
            explore_module()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()