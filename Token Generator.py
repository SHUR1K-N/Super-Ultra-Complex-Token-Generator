import requests; import re
import random; import time

URL = "https://raw.githubusercontent.com/SHUR1K-N/Super-Ultra-Secret-Tokens/main/tokens.txt?token=AKGUEVLXHEIBH6QA2VOACB3AED5NA"


tokensGrab = requests.get(URL)
tokensGrab = str(tokensGrab.content)
tokenList = re.findall(r"\\n([A-Z a-z]+-[0-9]+)", tokensGrab)

print(f"Your token is: {random.choice(tokenList)}")
print("\nPress Enter to exit.")
input()
