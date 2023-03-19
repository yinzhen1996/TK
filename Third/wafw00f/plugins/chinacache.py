
NAME = 'ChinaCache Load Balancer (ChinaCache)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Powered-By-ChinaCache', '.+'))
    ]
    if any(i for i in schemes):
        return True
    return False