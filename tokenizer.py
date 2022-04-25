from collections import defaultdict
from bs4 import BeautifulSoup
import re


def isNotAStopWord(token):
    stopWords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "areas", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "cannot", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "me", "more", "most", "my", "myself",
                 "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "should", "so", "some", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "with", "would", "you", "your", "yours", "yourself", "yourselves"]
    if token in stopWords:
        return False
    return True


def parse_text(text_string):
    # The list of tokens
    tokens = []
    # The individual token the below loop works with
    token = ""
    # Loop through all characters from a website's text
    for char in text_string:
        # If a character is alphanumeric, add it to the individual token
        if re.match('^[a-zA-Z0-9]+$', char):
            token += char
        # If a character is not alphanumeric, begin to append to one of the lists
        else:
            # If the existing token is alphanumeric
            if re.match('^[a-zA-Z0-9]+$', token):
                # Add the individual token (in lowercase) to the list of tokens
                tokens.append(token.lower())
                # Reset the individual token for the next for loop parse
                token = ""
    if re.match('^[a-zA-Z0-9]+$', token):
        if token.lower() not in tokens:
            tokens.append(token.lower())
    tokens = list(set(tokens))

    return tokens


def parseTextNoStopWords(text_string):
    # The list of tokens without stop words
    tokensNoStopWords = []
    # The individual token the below loop works with
    token = ""
    # Loop through all characters from a website's text
    for char in text_string:
        # If a character is alphanumeric, add it to the individual token
        if re.match('^[a-zA-Z0-9]+$', char):
            token += char
        # If a character is not alphanumeric, begin to append to one of the lists
        else:
            # If the existing token is alphanumeric
            if re.match('^[a-zA-Z0-9]+$', token):
                # If the individual token is not a stop word
                if(isNotAStopWord(token.lower())):
                    tokensNoStopWords.append(token.lower())
                # Reset the individual token for the next for loop parse
                token = ""
    if re.match('^[a-zA-Z0-9]+$', token):
        if token.lower() not in tokensNoStopWords:
            if(isNotAStopWord(token.lower())):
                tokensNoStopWords.append(token.lower())
    tokensNoStopWords = list(set(tokensNoStopWords))

    return tokensNoStopWords


def tokenize(html_file):
    soup = BeautifulSoup(html_file, "html.parser")
    text_string = soup.get_text(strip=True)
    tokens = parse_text(text_string)
    return tokens


def tokenizeNoStopWords(html_file):
    soup = BeautifulSoup(html_file, "html.parser")
    text_string = soup.get_text(strip=True)
    tokensNoStopWords = parseTextNoStopWords(text_string)
    return tokensNoStopWords


def computeWordFrequencies(tokenList):
    frequencies = defaultdict(int)
    for i in range(len(tokenList)):
        frequencies[tokenList[i]] += 1
    return frequencies
