

NAME = 'LimeLight CDN (LimeLight)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^limelight'),
        self.matchCookie(r'^l[mg]_sessid=')
    ]
    if any(i for i in schemes):
        return True
    return False 