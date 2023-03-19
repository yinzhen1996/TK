
NAME = 'Chuang Yu Shield (Yunaq)'


def is_waf(self):
    schemes = [
        self.matchContent(r'www\.365cyd\.com'),
        self.matchContent(r'help\.365cyd\.com/cyd\-error\-help.html\?code=403')
    ]
    if any(i for i in schemes):
        return True
    return False