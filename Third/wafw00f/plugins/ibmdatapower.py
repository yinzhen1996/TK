

NAME = 'DataPower (IBM)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Backside-Transport', r'(OK|FAIL)'))
    ]
    if any(i for i in schemes):
        return True
    return False