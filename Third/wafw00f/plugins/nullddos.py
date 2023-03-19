

NAME = 'NullDDoS Protection (NullDDoS)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'NullDDoS(.System)?'))
    ]
    if any(i for i in schemes):
        return True
    return False