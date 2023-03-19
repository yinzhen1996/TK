

NAME = 'Eisoo Cloud Firewall (Eisoo)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'EisooWAF(\-AZURE)?/?')),
        self.matchContent(r'<link.{0,10}?href=\"/eisoo\-firewall\-block\.css'),
        self.matchContent(r'www\.eisoo\.com'),
        self.matchContent(r'&copy; \d{4} Eisoo Inc')
    ]
    if any(i for i in schemes):
        return True
    return False