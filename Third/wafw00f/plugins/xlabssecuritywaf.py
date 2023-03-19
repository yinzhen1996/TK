

NAME = 'XLabs Security WAF (XLabs)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-CDN', r'XLabs Security')),
        self.matchHeader(('Secured', r'^By XLabs Security')),
        self.matchHeader(('Server', r'XLabs[-_]?.?WAF'), attack=True)
    ]
    if any(i for i in schemes):
        return True
    return False