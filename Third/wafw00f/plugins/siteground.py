

NAME = 'SiteGround (SiteGround)'


def is_waf(self):
    schemes = [
        self.matchContent(r"Our system thinks you might be a robot!"),
        self.matchContent(r'access is restricted due to a security rule')
    ]
    if any(i for i in schemes):
        return True
    return False