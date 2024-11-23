import requests
import string
import time
import random
from datetime import datetime

#"""

# by
# insta sir.sv7 
# discord u_nt
# gihub sir-sv7

#"""
def rFoR():
    return datetime(random.randint(1884, 2024), random.randint(1, 12), random.randint(1, 28)).isoformat() + 'Z'

def uFoU(username):
    url = "https://auth.roblox.com/v1/usernames/validate"
    h3 = {"User-Agent": "Mozilla/5.0", "Accept": "*/*"}
    d3 = {"birthday": rFoR(), "context": "Signup", "username": username}
    Fop = requests.get(url, headers=h3, params=d3)
    if Fop.status_code != 200:
        return f"{username}: Failed to connect to the server"
    data = Fop.json()
    messages = {
        "Username is already in use": "Username is already in use",
        "Username not appropriate for Roblox": "Username not appropriate for Roblox",
        "Username is valid": "Username is valid",
        "Usernames can have at most one _": "Usernames can have at most one _",
        "Only a-z, A-Z, 0-9, and _ are allowed": "Only a-z, A-Z, 0-9, and _ are allowed",
        "Usernames can be 3 to 20 characters long": "Usernames can be 3 to 20 characters long"
    }
    return f"{username}: {next((msg for key, msg in messages.items() if key in data.values()), 'Unknown error')}"

def gFoG(length=5):
    characters = string.ascii_lowercase + string.digits
    while True:
        random_chars = ''.join(random.choices(characters, k=length - 1))
        underscore_position = random.randint(0, length - 1)
        username = random_chars[:underscore_position] + '_' + random_chars[underscore_position:]
        yield username

for username in gFoG():
    print(uFoU(username))
    time.sleep(1)
