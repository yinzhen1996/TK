

NAME = 'Puhui (Puhui)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'Puhui[\-_]?WAF'))
    ]
    if any(i for i in schemes):
        return True
    return False