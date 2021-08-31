import requests; import re
import random; import time
import pyperclip

with open("ref.file", "r") as file:
    URL = file.readlines()

tokensGrab = requests.get(URL[0])
tokensGrab = str(tokensGrab.content)
tokenList = re.findall(r"\\n([A-Z a-z]+-[0-9]+)", tokensGrab)

token = random.choice(tokenList)
pyperclip.copy(token)

print(f"Your token is: {token} (automatically copied to your clipboard)")
print("\nPress Enter to exit.")
input()
