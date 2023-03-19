

NAME = 'Tencent Cloud Firewall (Tencent Technologies)'


def is_waf(self):
    schemes = [
        self.matchContent(r'waf\.tencent\-?cloud\.com/')
    ]
    if any(i for i in schemes):
        return True
    return False