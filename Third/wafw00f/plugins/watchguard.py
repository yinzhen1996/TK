
NAME = 'WatchGuard (WatchGuard Technologies)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', 'WatchGuard')),
        self.matchContent(r"Request denied by WatchGuard Firewall"),
        self.matchContent(r'WatchGuard Technologies Inc\.')
    ]
    if any(i for i in schemes):
        return True
    return False