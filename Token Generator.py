import requests; import re
import random; import time
import pyperclip

URL = "https://pastebin.com/raw/1T6y5XXT"

tokensGrab = requests.get(URL)
tokensGrab = str(tokensGrab.content)
tokenList = re.findall(r"\\n([A-Z a-z]+-[0-9]+)", tokensGrab)

token = random.choice(tokenList)
pyperclip.copy(token)

print(f"Your token is: {token} (automatically copied to your clipboard)")
print("\nPress Enter to exit.")
input()
