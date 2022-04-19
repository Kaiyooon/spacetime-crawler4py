# Jake's PartA tokenizer
# Please replace with yours if it is faster!

# Filter out HTML brackets
# Find a way to filter out (and store) subdomains (Question 4)

from collections import defaultdict
from bs4 import BeautifulSoup
import re

def parse_text(text_string):
    tokens = []
    token = ""
    for char in text_string:
        if re.match('^[a-zA-Z0-9]+$', char):
                token += char
        else:
            if re.match('^[a-zA-Z0-9]+$', token):
                tokens.append(token.lower())
                token = ""
    if re.match('^[a-zA-Z0-9]+$', token):
        if token.lower() not in tokens:
            tokens.append(token.lower())
    tokens = list(set(tokens))

    return tokens

def tokenize(html_file):
    soup = BeautifulSoup(html_file, "html.parser")
    tokens = ["foo"]

    text_string = soup.get_text(strip=True)
    tokens = parse_text(text_string)
    print(tokens)
    return tokens

def computeWordFrequencies(tokenList):
    frequencies = defaultdict(int)
    for i in range(len(tokenList)):
        frequencies[tokenList[i]] += 1
    return frequencies
