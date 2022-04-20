def getSchemeAndDomain(hyperlink):
    # Split the first 3 "/" into separate strings,
    # for a total of 4 strings. "http(s):" as index 0, "" as index 1, domain as
    # index 2, everything else as index 3.
    #
    # Outside code used to assist with navigating .split:
    # https://www.w3schools.com/python/ref_string_split.asp
    temporaryString = hyperlink.split("/",3)
    # appends with "https:" or "http:""
    returnableString = temporaryString[0]
    # appends with "//"
    returnableString.append("//")
    # appends with domain
    returnableString.append(temporaryString[2])

    return returnableString
