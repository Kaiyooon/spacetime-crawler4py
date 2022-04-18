

class unique:
    uniquePages = set()


class longest:
    longestPage = ""
    longestPageLength = 0


class common:
    commonWords = {}


class subdomains:
    subdomains = {}

    def convert():
        subdomainlist = []
        for key, value in sorted(subdomains.subdomains.items()):
            subdomainlist.append(f"{key}, {value}")
        return subdomainlist
