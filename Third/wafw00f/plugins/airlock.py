NAME = 'Airlock (Phion/Ergon)'


def is_waf(self):
    schemes = [
        # This method of detection is old (though most reliable), so we check it first
        self.matchCookie(r'^al[_-]?(sess|lb)='),
        self.matchContent(r'server detected a syntax error in your request')
        ]
    if any(i for i in schemes):
        return True
    return False