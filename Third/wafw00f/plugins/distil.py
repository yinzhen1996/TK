

NAME = 'Distil (Distil Networks)'


def is_waf(self):
    schemes = [
        self.matchContent(r'cdn\.distilnetworks\.com/images/anomaly\.detected\.png'),
        self.matchContent(r'distilCaptchaForm'),
        self.matchContent(r'distilCallbackGuard')
    ]
    if any(i for i in schemes):
        return True
    return False