
NAME = 'Comodo cWatch (Comodo CyberSecurity)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'Protected by COMODO WAF(.+)?'))
    ]
    if any(i for i in schemes):
        return True
    return False