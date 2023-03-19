

NAME = 'Zenedge (Zenedge)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'ZENEDGE')),
        self.matchHeader(('X-Zen-Fury', r'.+?')),
        self.matchContent(r'/__zenedge/')
    ]
    if any(i for i in schemes):
        return True
    return False