
NAME = 'BitNinja (BitNinja)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Security check by BitNinja'),
        self.matchContent(r'Visitor anti-robot validation')
    ]
    if any(i for i in schemes):
        return True
    return False