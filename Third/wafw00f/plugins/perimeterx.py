
NAME = 'PerimeterX (PerimeterX)'


def is_waf(self):
    schemes = [
        self.matchContent(r'www\.perimeterx\.(com|net)/whywasiblocked'),
        self.matchContent(r'client\.perimeterx\.(net|com)'),
        self.matchContent(r'denied because we believe you are using automation tools')
    ]
    if any(i for i in schemes):
        return True
    return False