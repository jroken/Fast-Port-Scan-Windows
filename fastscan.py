import os
while True:
    os.system("cls")
    ip = input("Enter Website Or İp :  ")
    os.system(f"nmap {ip}")
    print("")
    print("Press enter to continue")
    input("")
    os.system("cls")
