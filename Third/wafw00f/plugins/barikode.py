

NAME = 'Barikode (Ethic Ninja)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<strong>barikode<.strong>'),
    ]
    if any(i for i in schemes):
        return True
    return False