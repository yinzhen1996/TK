

NAME = 'Azure Front Door (Microsoft)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Azure-Ref', '.+?')),
    ]
    if any(i for i in schemes):
        return True
    return False