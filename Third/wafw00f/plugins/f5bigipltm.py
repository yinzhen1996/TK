

NAME = 'BIG-IP Local Traffic Manager (F5 Networks)'


def is_waf(self):
    schemes = [
        self.matchCookie('^bigipserver'),
        self.matchHeader(('X-Cnection', 'close'), attack=True)
    ]
    if any(i for i in schemes):
        return True
    return False