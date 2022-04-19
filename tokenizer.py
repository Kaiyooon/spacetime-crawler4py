# Jake's PartA tokenizer
# Please replace with yours if it is faster!

# Filter out HTML brackets
# Find a way to filter out (and store) subdomains (Question 4)

from collections import defaultdict

def tokenize(filename):
    pass


def computeWordFrequencies(tokenList):
    frequencies = defaultdict(int)
    for i in range(len(tokenList)):
        frequencies[tokenList[i]] += 1
    return frequencies
