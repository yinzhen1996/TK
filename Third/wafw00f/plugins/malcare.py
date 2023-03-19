

NAME = 'Malcare (Inactiv)'


def is_waf(self):
    schemes = [
        self.matchContent(r'firewall.{0,15}?powered.by.{0,15}?malcare.{0,15}?pro'),
        self.matchContent('blocked because of malicious activities')
    ]
    if any(i for i in schemes):
        return True
    return False