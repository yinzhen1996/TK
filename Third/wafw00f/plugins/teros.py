

NAME = 'Teros (Citrix Systems)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^st8id=')
    ]
    if any(i for i in schemes):
        return True
    return False