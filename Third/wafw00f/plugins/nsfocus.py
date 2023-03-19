
NAME = 'NSFocus (NSFocus Global Inc.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'NSFocus'))
    ]
    if any(i for i in schemes):
        return True
    return False