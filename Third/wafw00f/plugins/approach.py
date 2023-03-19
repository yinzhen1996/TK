
NAME = 'Approach (Approach)'


def is_waf(self):
    schemes = [
        # This method of detection is old (though most reliable), so we check it first
        self.matchContent(r'approach.{0,10}?web application (firewall|filtering)'),
        self.matchContent(r'approach.{0,10}?infrastructure team')
        ]
    if any(i for i in schemes):
        return True
    return False