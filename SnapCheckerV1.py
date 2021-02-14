# -*- coding:utf -8 -*-
# get line
# for
import requests
import time as mm
import sys as n
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
def slow(M): ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)
slow(O +'''
███████╗███╗   ██╗ █████╗ ██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗     ██╗   ██╗ ██╗
██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║███║
███████╗██╔██╗ ██║███████║██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝    ██║   ██║╚██║
╚════██║██║╚██╗██║██╔══██║██╔═══╝     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝ ██║
███████║██║ ╚████║██║  ██║██║         ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║     ╚████╔╝  ██║
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═══╝   ╚═╝
   Free Version By : Xcode                                                                                                                                                                 
''')

slow(O+'''
                    ▒▒▒▒▒▒▒▒▒▒                    
                ▒▒▒▒░░      ░░▒▒▒▒                
              ▒▒░░              ░░▒▒              
            ▒▒░░                  ░░▒▒            
            ▒▒                      ▒▒            
  ▒▒      ▒▒░░              ████    ░░▒▒      ▒▒  
▒▒░░▒▒    ▒▒░░            ████████  ░░▒▒    ▒▒░░▒▒
▒▒░░░░▒▒  ▒▒░░  ██▓▓    ██▓▓▓▓▓▓████░░▒▒  ▒▒░░░░▒▒
▒▒░░  ░░▒▒▒▒░░  ▓▓▓▓    ██▓▓▒▒▒▒▓▓██░░▒▒░░░░  ░░▒▒
  ▒▒    ░░▒▒░░            ██▓▓▓▓▓▓  ░░▒▒░░    ▒▒  
  ▒▒░░    ▒▒░░                      ░░▒▒      ▒▒  
    ░░    ▒▒░░  ██              ██  ░░▒▒    ▒▒    
    ▒▒░░░░▒▒░░    ██▓▓▒▒▓▓▒▒▓▓██    ░░▒▒░░░░▒▒    
      ▒▒░░▒▒░░      ▒▒▒▒▒▒▒▒▒▒      ░░▒▒░░░░      
        ▒▒░░        ▒▒░░░░░░▒▒        ░░▒▒        
        ▒▒░░░░  ░░░░▒▒░░░░░░▒▒░░░░  ░░░░▒▒        
        ▒▒░░░░░░░░░░▒▒░░░░░░▒▒░░░░░░░░░░▒▒        
        ▒▒░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░▒▒        
      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒      
      ▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒      
    ▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒    
  ▓▓▒▒▒▒▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▒▒▓▓  
    ▒▒▒▒▒▒            ▒▒▒▒▒▒            ▒▒▒▒▒▒    
------------------------------------------------------------------------
#Coded By : Xcode & Twitter: @XcodeOn1 
''')

print(" \n ")

def getUser(Username):
    url = "https://app.snapchat.com:443/loq/suggest_username_v2"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
               "Accept": "application/json", "Accept-Locale": "en_SA", "Connection": "close",
               "X-Snapchat-UUID": "",
               "x-snapchat-att": "CgsYACAAFaiThEQIChK4AXyUc_6dfBtKSeUR7bYZn0xI3IaxCqocThfdZ4fCFeoM8mrMEximQTGWrkzcyg1sjaRpG4u1K0n7-Next7xsXOUxyVojGVG1gu6BZ8_cFt0q-JMVpYEUrN6IIab-cKS9_5WiHel0tW6U04TmiXOac9dHtkIgbvF0w9J6vq3XxA8_IEF6ibfu2qkBZxvaRuCrEzZh-4GFEo_0BM6m2dJmTZTxTw5xxKwlGBIXq_yqQ7Ba-v8lfOEEzdw=",
               "User-Agent": "Snapchat/10.87.0.69 (Twitter XcodeOn1; iOS 13.5.1; gzip)",
               "Accept-Language": "en-SA;q=1, ar-SA;q=0.9, en-US;q=0.8, bn-SA;q=0.7, pa-SA;q=0.6",
               "Accept-Encoding": "gzip, deflate"}
    web_data = {"req_token": "9307955c05e1ab886e3a9eeff7a501f40deb4d8219ac0a87f9b4f214dfc518eb",
                "requested_username": Username, "timestamp": "1595566579397"}
    response = requests.post(url, headers=headers, data=web_data)
    if (response.status_code == 200):
        data = response.json()
        # print(type(data))
        # print("status_code is ")
        if (data["status_code"] == "OK"):
            print(GR + "Found" )
            with open('UserFound.txt', 'a') as x:
                x.write(Username + '\n')
        else:
            print(R + " Not Found")
        print(W +"#" * 50 + "By @xcodeone1")
        print(data)

file = open("Users.txt","r")
lines = file.readlines()
# print(type(lines))
# print(lines)
for line in lines:
    line = str(line).strip()
    getUser(line)
Snapchat: m.pg 
Snapchat: siid 
Snapchat : xbce 
Snapchat: y3g
