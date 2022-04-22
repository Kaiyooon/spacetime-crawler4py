

class unique:
    uniquePages = set()


class longest:
    longestPage = ""
    longestPageLength = 0


class common:
    commonWords = {}

    def calculate(newDict):
        for key, value in newDict.items():
            if key in common.commonWords.keys():
                common.commonWords[key] += value
            else:
                common.commonWords[key] = value


class subdomains:
    subdomainLinks = {}
    subdomains = set()

    def convert():
        subdomainlist = []
        for key, value in sorted(subdomains.subdomainLinks.items()):
            subdomainlist.append(f"{key}, {len(value)}")
        return subdomainlist


class simhash_data:
    data = {}
    # we need a unique key so we'll just use a counter
    uniqueID = 0
