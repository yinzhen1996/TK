NAME = 'AireeCDN (Airee)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Airee')),
        self.matchHeader(('X-Cache', r'(\w+\.)?airee\.cloud')),
        self.matchContent(r'airee\.cloud')
    ]
    if any(i for i in schemes):
        return True
    return False