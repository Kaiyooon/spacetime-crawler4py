'''
================================================================================
TO-DO:
================================================================================

** ADD UCI ID'S TO CONFIG.INI FOLLOWING THE FORMAT **

=====================
Functionality Oriented:
=====================
* URL Behavior:
    * Transform URLs from relative to absolute
    * Send server requests with an ASCII URL and neither the HTML content of the
      webpage that we are crawling nor UNICODE strings.
* In "is_valid(url)", return "False" if not from the specified domains:
    * *.ics.uci.edu/*
    * *.cs.uci.edu/*
    * *.informatics.uci.edu/*
    * *.stat.uci.edu/*
    * today.uci.edu/department/information_computer_sciences/*
* Write a simple automatic trap detection system based on URL patterns and/or
    content similarity or repetition over a certain amount of chained pages.
* Detect and avoid sets of similar pages with no information.
* Detect and avoid dead URLs that return a 200 status but no data
======================
Report Oriented:
======================
( Think about how to export these.... create .txt files somehwere upon completion
  of crawling? )

* Record number of unique pages (subdomains. ex: http://www.ics.uci.edu#aaa and
  http://www.ics.uci.edu#bbb are the same URL for these purposes)
* Record longest page in terms of the number of words (HTML markup doesn't count
  as words)
* Record 50 most common words in the entire set of pages (IGNORING English stop words,
  found here: https://www.ranks.nl/stopwords).
    * Order these by frequency
* Record the number of ics.uci.edu subdomains
    * Order these alphabetically and by the number of unique pages in each subdomain

================================================================================
IDEAS:
================================================================================

* For the return of extract_next_links():
    * Use resp.(raw_response.(content.(txt))) to get a dictionary of HTML content.
        * This can be parsed w/keys
        * From https://realpython.com/python-requests/#the-response

================================================================================
QUESTIONS FOR TA:
================================================================================

* Is the definition of "page" the same for Questions 1, 2, and 3?
    * Yes, but interpretations are different depending on unique vs. not unique.
    * So Q1 ignores anything after the .edu (in the example), but Q2 and Q3 don't.
* For Question #4, do we order first alphabetically, then by unique pages?
    * as long as we do it alphabetically. TA just matches results against theirs.
* EC +2 pts: Can use beautifulsoup to extract content. CANNOT USE library for
    * detecting similarity, but can use to extract content.
* Get response from the forked class
* Call .content on scacetime crawler's Response class to get the content
    * Beautiful soup gets all content of a page as well
* Multithreading resources (TA couldn't help, but could point to resources):
    * https://www.educba.com/python-threadpool/
    * https://docs.python.org/3/library/threading.html
* Can create new .py files
* Format does not matter for the deliverables (Q#1-4) (as long as it's readable)
'''

import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    hyperlinks = list()
    if resp.status == 200:
        # Use BeautifulSoup to filter links from content
        soup = BeautifulSoup(resp.raw_response.content, 'html.parser')
        for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
            hyperlinks.append(link.get('href'))
        print(hyperlinks)
    hyperlinks = list()
    return hyperlinks

def is_valid(url):
    # Decide whether to crawl this url or not.
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
