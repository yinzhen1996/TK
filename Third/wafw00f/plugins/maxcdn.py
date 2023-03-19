
NAME = 'MaxCDN (MaxCDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-CDN', r'maxcdn'))
    ]
    if any(i for i in schemes):
        return True
    return False