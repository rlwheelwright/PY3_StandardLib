# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request # Class we're going to use
import json
import textwrap

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
    text = f.read()
    decodedText = text.decode('utf-8') # Decode so we can print to user
    print(textwrap.fill(decodedText, width=50))

print()

obj = json.loads(decodedText)
print(obj['kind'])
print(obj['items'][0]['searchInfo']['textSnippet'])
