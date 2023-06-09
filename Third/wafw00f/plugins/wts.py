

NAME = 'WTS-WAF (WTS)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'wts/[0-9\.]+?')),
        self.matchContent(r"<(title|h\d{1})>WTS\-WAF")
    ]
    if any(i for i in schemes):
        return True
    return False