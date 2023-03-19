
NAME = 'KeyCDN (KeyCDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'KeyCDN'))
    ]
    if any(i for i in schemes):
        return True
    return False