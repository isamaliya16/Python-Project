def write_file() :
    name = input("Enter file  name : ")
    data = input("Enter content : ")
    with open(name,"w") as f :
        f.write(data)
        print("File written content . ")
        
def read_file():
    name = input("Enter the File Name : ")
    try : 
        with open(name,"r") as f : 
            print("File content : \n ",f.read())
    except FileExistsError: 
        print("File not found !")
    
def file_menu():
    print("\n 1.Write File ")
    print("2.Read File")
    
    ch = input("Enter chioce :")
    if ch == '1':
        write_file()
    elif ch == '2': 
        read_file()
        


        