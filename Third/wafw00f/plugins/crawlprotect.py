
NAME = 'CrawlProtect (Jean-Denis Brun)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^crawlprotecttag='),
        self.matchContent(r'<title>crawlprotect'),
        self.matchContent(r'this site is protected by crawlprotect')
    ]
    if any(i for i in schemes):
        return True
    return False