
NAME = 'WebARX (WebARX Security Solutions)'


def is_waf(self):
    schemes = [
        self.matchContent(r"WebARX.{0,10}?Web Application Firewall"),
        self.matchContent(r"www\.webarxsecurity\.com"),
        self.matchContent(r'/wp\-content/plugins/webarx/includes/')
    ]
    if any(i for i in schemes):
        return True
    return False