from simhash import Simhash, SimhashIndex
import re
from classes import simhash_data


def getSchemeAndDomain(hyperlink):
    # Split the first 3 "/" into separate strings,
    # for a total of 4 strings. "http(s):" as index 0, "" as index 1, domain as
    # index 2, everything else as index 3.
    #
    # Outside code used to assist with navigating .split:
    # https://www.w3schools.com/python/ref_string_split.asp
    temporaryString = hyperlink.split("/", 3)
    # appends with "https:" or "http:""
    returnableString = temporaryString[0]
    # appends with "//"
    returnableString += "//"
    # appends with domain
    returnableString += temporaryString[2]

    return returnableString

    # def getDomain(hyperlink):
    # # Outside code used to assist with navigating .split:
    # # https://www.w3schools.com/python/ref_string_split.asp
    # temporaryString = hyperlink.split("/", 3)
    # # appends with domain
    # returnableString = temporaryString[2]

    # return returnableString


def extractSubdomain(domain):
    splitPeriod = domain.split('.')
    splitSubdomain = splitPeriod[:-3]
    return '.'.join(splitSubdomain)

# Outside code used:
# https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]


def check_dups(content):
    if len(content) > 50000:
        content = content[:50000]
    s = Simhash(get_features(content))
    # Outside code used below:
    # https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
    objs = [(str(k), Simhash(get_features(v)))
            for k, v in simhash_data.data.items()]
    index = SimhashIndex(objs, k=3)
    if len(index.get_near_dups(s)) == 0:
        simhash_data.data[simhash_data.uniqueID] = content
        simhash_data.uniqueID += 1
        return False
    return True
