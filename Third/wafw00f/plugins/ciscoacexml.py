
NAME = 'ACE XML Gateway (Cisco)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'ACE XML Gateway'))
    ]
    if any(i for i in schemes):
        return True
    return False