

NAME = 'SiteGuard (Sakura Inc.)'


def is_waf(self):
    schemes = [
        self.matchContent(r"Powered by SiteGuard"),
        self.matchContent(r'The server refuse to browse the page')
    ]
    if any(i for i in schemes):
        return True
    return False