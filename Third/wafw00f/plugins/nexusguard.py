

NAME = 'NexusGuard Firewall (NexusGuard)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Powered by Nexusguard'),
        self.matchContent(r'nexusguard\.com/wafpage/.+#\d{3};')
    ]
    if any(i for i in schemes):
        return True
    return False