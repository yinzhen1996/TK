

NAME = 'Kona SiteDefender (Akamai)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'AkamaiGHost')),
        self.matchHeader(('Server', 'AkamaiGHost'), attack=True)        
    ]
    if any(i for i in schemes):
        return True
    return False