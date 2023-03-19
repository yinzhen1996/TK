

NAME = 'NevisProxy (AdNovum)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^Navajo'),
        self.matchCookie(r'^NP_ID')
    ]
    if any(i for i in schemes):
        return True
    return False