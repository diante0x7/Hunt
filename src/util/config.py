import json
import os

def parse_config():
    try:
        with open("config.json", "r") as fp:
            data = json.loads(fp.read())
    except:
        #print("File not found. Download config.json from the github and reformat it.")
        return False
    
    try:
        token = data['application']['token']
        upcoming = data['application']['upcoming']
    except:
        #print("KeyError. Please redownload the config.json.")
        return False
                
    return {
        "token": token,
        "upcoming": upcoming
    }

def create_config(token, upcoming):
    try:
        os.remove(".config.json") # remove current config, if any
    except:
        True

    data = json.dumps({'application':
                {'token': token,
                 'upcoming': upcoming}})
    
    with open("config.json", 'w+') as fp:
        fp.write(data)

    return True

def about_me():
    return ["""
I am the CougarCS InfoSec Helper <:infosec:1150607912532721785>! Currently, I am in alpha version 0.1. 
            
I am a modified, more refined version that combines the features of 3 template bots designed by Nathan Hunt and Diante Jackson. Over time, this bot will evolve to contain all the necessary functions and tools needed to help infosec flourish!
""",
"""
I feature an offline shellcrafting tool to help you in your penetration testing escapades!
Reverse Shells:
- Python
- Bash
- PHP
- Netcat (traditional and bsd)
""",
"""
I can also search for relevant CVE's based on some keywords, or give you information about specific CVE's based on their unique ID.
""",
"""
Soon, I will be perfectly capable of listing out upcoming CTF Events as they become available, giving infosec members the opportunity to form teams and work together on challenges and machines!
""",
"""
Project available at https://github.com/diante0x7/Hunt
"""]

def get_uptime(start_time, current_time):
    td = current_time - start_time
    return "Hunt has been running for {} days, {} hours, {} minutes, and {} seconds.".format(
        td.days, td.seconds//3600, td.seconds//60, td.seconds % 60
    )