
NAME = 'Fastly (Fastly CDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Fastly-Request-ID', r'\w+'))
    ]
    if any(i for i in schemes):
        return True
    return False