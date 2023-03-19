
NAME = 'PentaWAF (Global Network Services)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'PentaWaf(/[0-9\.]+)?')),
        self.matchContent(r'Penta.?Waf/[0-9\.]+?.server')
    ]
    if any(i for i in schemes):
        return True
    return False