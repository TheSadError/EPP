from colorama import *
from time import sleep 
import os 

def menu(login):
    if login==True:
        print(Fore.BLUE+"""{- Hi! Welcome To EPP (E++). Please choice : -}
        
        [1] Anti Virus{
            [1] File Scan
            [2] Url  Scan    
        }
        
        """)
def epp():
    login = True
    menu(login)
    
    n = input(Fore.RED+"[+] Please select : ")
    if n=="1":
        os.system("python3 ./Epp/antiv.py")
    
if __name__ == '__main__':
    print(Fore.BLUE+"[!] Hi, Welcome to E++ !")
    os.system("clear")
    epp()