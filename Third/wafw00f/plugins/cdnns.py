

NAME = 'CdnNS Application Gateway (CdnNs/WdidcNet)'


def is_waf(self):
    schemes = [
        self.matchContent(r'cdnnswaf application gateway')
    ]
    if any(i for i in schemes):
        return True
    return False