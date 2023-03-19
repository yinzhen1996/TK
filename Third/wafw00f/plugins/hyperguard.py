

NAME = 'HyperGuard (Art of Defense)'


def is_waf(self):
    schemes = [
        self.matchCookie('^WODSESSION=')
    ]
    if any(i for i in schemes):
        return True
    return False