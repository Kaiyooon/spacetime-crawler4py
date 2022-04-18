

class unique:
    uniquePages = set()


class longest:
    longestPage = ""
    longestPageLength = 0


class common:
    commonWords = {}


class subdomains:
    subdomainLinks = {}
    subdomains = set()

    def convert():
        subdomainlist = []
        for key, value in sorted(subdomains.subdomainLinks.items()):
            subdomainlist.append(f"{key}, {value}")
        return subdomainlist
