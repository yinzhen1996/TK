

NAME = 'Profense (ArmorLogic)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Profense')),
        self.matchCookie(r'^PLBSID=')
    ]
    if any(i for i in schemes):
        return True
    return False