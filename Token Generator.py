import requests; import re
import random; import time
import pyperclip

grabURL = requests.get("https://raw.githubusercontent.com/SHUR1K-N/Super-Ultra-Complex-Token-Generator/main/ref.file")
grabURL = str(grabURL.content)
URL = re.findall(r"b'(.+)\'", grabURL)

grabTokens = requests.get(URL[0])
grabTokens = str(grabTokens.content)
tokenList = re.findall(r"\\n([A-Z a-z]+-[0-9]+)", grabTokens)

token = random.choice(tokenList)
pyperclip.copy(token)

print(f"Your token is: {token} (automatically copied to your clipboard)")
print("\nPress Enter to exit.")
input()
