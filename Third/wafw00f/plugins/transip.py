

NAME = 'TransIP Web Firewall (TransIP)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-TransIP-Backend', '.+')),
        self.matchHeader(('X-TransIP-Balancer', '.+'))
    ]
    if any(i for i in schemes):
        return True
    return False