

NAME = 'Safeline (Chaitin Tech.)'


def is_waf(self):
    schemes = [
        self.matchContent(r'safeline|<!\-\-\sevent id:')
    ]
    if any(i for i in schemes):
        return True
    return False