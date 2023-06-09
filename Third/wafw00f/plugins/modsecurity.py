

NAME = 'ModSecurity (SpiderLabs)'


def is_waf(self):
    schema1 = [
        self.matchHeader(('Server', r'(mod_security|Mod_Security|NOYB)')),
        self.matchContent(r'This error was generated by Mod.?Security'),
        self.matchContent(r'rules of the mod.security.module'),
        self.matchContent(r'mod.security.rules triggered'),
        self.matchContent(r'Protected by Mod.?Security'),
        self.matchContent(r'/modsecurity[\-_]errorpage/'),
        self.matchContent(r'modsecurity iis')
    ]
    schema2 = [
        self.matchReason('ModSecurity Action'),
        self.matchStatus(403)
    ]
    schema3 = [
        self.matchReason('ModSecurity Action'),
        self.matchStatus(406)
    ]
    if any(i for i in schema1):
        return True
    if all(i for i in schema2):
        return True
    if all(i for i in schema3):
        return True
    return False