

NAME = 'BIG-IP AppSec Manager (F5 Networks)'


def is_waf(self):
    schemes = [
        self.matchContent('the requested url was rejected'),
        self.matchContent('please consult with your administrator')
    ]
    if all(i for i in schemes):
        return True
    return False