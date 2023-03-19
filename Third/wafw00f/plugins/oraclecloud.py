
NAME = 'Oracle Cloud (Oracle)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<title>fw_error_www'),
        self.matchContent(r'src=\"/oralogo_small\.gif\"'),
        self.matchContent(r'www\.oracleimg\.com/us/assets/metrics/ora_ocom\.js')
    ]
    if any(i for i in schemes):
        return True
    return False