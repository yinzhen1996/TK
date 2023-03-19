

NAME = 'Mission Control Shield (Mission Control)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'Mission Control Application Shield'))
    ]
    if any(i for i in schemes):
        return True
    return False