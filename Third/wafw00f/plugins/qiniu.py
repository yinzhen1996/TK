
NAME = 'Qiniu (Qiniu CDN)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-Qiniu-CDN', r'\d+?'))
    ]
    if any(i for i in schemes):
        return True
    return False