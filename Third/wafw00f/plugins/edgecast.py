

NAME = 'Edgecast (Verizon Digital Media)'


def is_waf(self):
    schemes = [
        self.matchHeader(('Server', r'^ECD(.+)?')),
        self.matchHeader(('Server', r'^ECS(.*)?'))
    ]
    if any(i for i in schemes):
        return True
    return False