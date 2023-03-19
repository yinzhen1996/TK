
NAME = 'WebLand (WebLand)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'protected by webland'))
    ]
    if any(i for i in schemes):
        return True
    return False