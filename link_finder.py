from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.baseURL = base_url
        self.pageURL = page_url
        self.links = set()

    def handle_starttag(self, tag, attributes):
        if tag == 'a':
            for(attribute, value) in attributes:
                if attribute == 'href':
                    url = parse.urljoin(self.baseURL, value)
                    self.links.add(url)

    def get_links(self):
        return self.links

    def error(self, message):
        pass
