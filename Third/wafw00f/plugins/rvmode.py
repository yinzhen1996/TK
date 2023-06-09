
NAME = 'RequestValidationMode (Microsoft)'


def is_waf(self):
    schemes = [
        self.matchContent(r'Request Validation has detected a potentially dangerous client input'),
        self.matchContent(r'ASP\.NET has detected data in the request'),
        self.matchContent(r'HttpRequestValidationException')
    ]
    if any(i for i in schemes):
        return True
    return False