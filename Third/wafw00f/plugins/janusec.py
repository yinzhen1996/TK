
NAME = 'Janusec Application Gateway (Janusec)'


def is_waf(self):
    schemes = [
        self.matchContent(r'janusec application gateway')
    ]
    if any(i for i in schemes):
        return True
    return False