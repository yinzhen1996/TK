

NAME = 'SecureSphere (Imperva Inc.)'


def is_waf(self):
    schemes = [
        self.matchContent(r'<(title|h2)>Error'),
        self.matchContent(r'The incident ID is'),
        self.matchContent(r"This page can't be displayed"),
        self.matchContent(r'Contact support for additional information')
    ]
    if all(i for i in schemes):
        return True
    return False