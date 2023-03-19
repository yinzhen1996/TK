
NAME = 'Viettel (Cloudrity)'


def is_waf(self):
    schemes = [
        self.matchContent(r"Access Denied.{0,10}?Viettel WAF"),
        self.matchContent(r"cloudrity\.com\.(vn)?/"),
        self.matchContent(r"Viettel WAF System")
    ]
    if any(i for i in schemes):
        return True
    return False