from colorama import *
from time import sleep 
import virustotal_python
import os.path
from pprint import pprint
from base64 import urlsafe_b64encode

def file(api):
    FILE_PATH = "C:"
    files = {"file": (os.path.basename(FILE_PATH), open(os.path.abspath(FILE_PATH), "rb"))}

    with virustotal_python.Virustotal(api) as vtotal:
        resp = vtotal.request("files", files=files, method="POST")
        pprint(resp.json())

def url(api):
    url = input("[!] Please input url : ")

    with virustotal_python.Virustotal(api) as vtotal:
        try:
            resp = vtotal.request("urls", data={"url": url}, method="POST")
            url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
            report = vtotal.request(f"urls/{url_id}")
            pprint(report.object_type)
            pprint(report.data)
        except virustotal_python.VirustotalError as err:
            print(f"Failed to send URL: {url} for analysis and get the report: {err}")

def antiv(api):
    print(Fore.BLUE+"[+] Hi, Please Select : ")
    print(Fore.RED+"""
    
    [1] File Scan
    [2] Url Scan         
""")
    n = input(Fore.RED+"[!] Please select : ")
    if n == "1":
        file(api)
    elif n == "2":
        url(api)
        
    
if __name__ == '__main__':
    os.system("clear")
    api = input(Fore.BLUE+"[+] Please input API key (Virus Total Key) : ")
    antiv(api)