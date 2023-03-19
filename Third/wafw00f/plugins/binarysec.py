
NAME = 'BinarySec (BinarySec)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'BinarySec')),
        self.matchHeader(('x-binarysec-via', '.+')),
        self.matchHeader(('x-binarysec-nocache', '.+'))
    ]
    if any(i for i in schemes):
        return True
    return False