
NAME = 'RayWAF (WebRay Solutions)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'WebRay\-WAF')),
        self.matchHeader(('DrivedBy', r'RaySrv.RayEng/[0-9\.]+?'))
    ]
    if any(i for i in schemes):
        return True
    return False