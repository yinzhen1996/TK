

NAME = 'eEye SecureIIS (BeyondTrust)'


def is_waf(self):
    schemes = [
        self.matchContent(r'SecureIIS is an internet security application'),
        self.matchContent(r'Download SecureIIS Personal Edition'),
        self.matchContent(r'https?://www\.eeye\.com/Secure\-?IIS')
    ]
    if any(i for i in schemes):
        return True
    return False