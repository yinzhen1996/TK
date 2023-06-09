
NAME = 'Bluedon (Bluedon IST)'


def is_waf(self):
    schemes = [
        # Found sample servers returning 'Server: BDWAF/2.0'
        self.matchHeader(('Server', r'BDWAF')),
        self.matchContent(r'bluedon web application firewall')
    ]
    if any(i for i in schemes):
        return True
    return False