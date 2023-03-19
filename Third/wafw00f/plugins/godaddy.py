
NAME = 'GoDaddy Website Protection (GoDaddy)'


def is_waf(self):
    schemes = [
        self.matchContent(r'GoDaddy (security|website firewall)')
    ]
    if any(i for i in schemes):
        return True
    return False