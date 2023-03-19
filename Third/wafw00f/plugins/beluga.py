

NAME = 'Beluga CDN (Beluga)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'Beluga')),
        self.matchCookie(r'^beluga_request_trail=')
    ]
    if any(i for i in schemes):
        return True
    return False