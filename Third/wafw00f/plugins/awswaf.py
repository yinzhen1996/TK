
NAME = 'AWS Elastic Load Balancer (Amazon)'


def is_waf(self):
    schemes = [
        self.matchHeader(('X-AMZ-ID', '.+?')),
        self.matchHeader(('X-AMZ-Request-ID', '.+?')),
        self.matchCookie(r'^aws.?alb='),
        self.matchHeader(('Server', r'aws.?elb'), attack=True)
    ]
    if any(i for i in schemes):
        return True
    return False