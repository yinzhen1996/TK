
NAME = 'Astra (Czar Securities)'


def is_waf(self):
    schemes = [
        self.matchCookie(r'^cz_astra_csrf_cookie'),
        self.matchContent(r'astrawebsecurity\.freshdesk\.com'),
        self.matchContent(r'www\.getastra\.com/assets/images')
    ]
    if any(i for i in schemes):
        return True
    return False