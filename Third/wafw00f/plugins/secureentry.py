
NAME = 'Secure Entry (United Security Providers)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Secure Entry Server'))
    ]
    if any(i for i in schemes):
        return True
    return False