

NAME = 'Shadow Daemon (Zecure)'


def is_waf(self):
    schemes = [
        self.matchContent(r"<h\d{1}>\d{3}.forbidden<.h\d{1}>"),
        self.matchContent(r"request forbidden by administrative rules")
    ]
    if all(i for i in schemes):
        return True
    return False