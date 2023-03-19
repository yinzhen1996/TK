
NAME = 'ASPA Firewall (ASPA Engineering Co.)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'ASPA[\-_]?WAF')),
        self.matchHeader(('ASPA-Cache-Status', r'.+?'))
    ]
    if any(i for i in schemes):
        return True
    return False