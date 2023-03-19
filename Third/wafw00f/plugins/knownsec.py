

NAME = 'KS-WAF (KnownSec)'


def is_waf(self):
    schemes = [
        self.matchContent(r'/ks[-_]waf[-_]error\.png')
    ]
    if any(i for i in schemes):
        return True
    return False