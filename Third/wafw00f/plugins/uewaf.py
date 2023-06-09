

NAME = 'UEWaf (UCloud)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'uewaf(/[0-9\.]+)?')),
        self.matchContent(r'/uewaf_deny_pages/default/img/'),
        self.matchContent(r'ucloud\.cn')
    ]
    if any(i for i in schemes):
        return True
    return False