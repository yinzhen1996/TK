
NAME = 'Trafficshield (F5 Networks)'


def is_waf(self):
    schemes = [
        self.matchCookie('^ASINFO='),
        self.matchHeader(('Server', 'F5-TrafficShield'))
    ]
    if any(i for i in schemes):
        return True
    return False