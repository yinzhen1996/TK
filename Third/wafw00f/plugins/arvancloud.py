

NAME = 'ArvanCloud (ArvanCloud)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'ArvanCloud'))
    ]
    if any(i for i in schemes):
        return True
    return False