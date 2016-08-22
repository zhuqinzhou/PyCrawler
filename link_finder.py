from html.parser import  HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self, baseURL, pageURL):
        super.__init__()
        self.baseURL = baseURL
        self.pageURL = pageURL
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.baseURL, value)
                    self.links.add(url)

    def getLinks(self):
        return self.links

    def error(self, message):
        pass
