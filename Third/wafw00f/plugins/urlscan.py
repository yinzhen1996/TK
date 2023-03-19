

NAME = 'URLScan (Microsoft)'


def is_waf(self):
    schemes = [
        self.matchContent(r"Rejected[-_]By[_-]UrlScan"),
        self.matchContent(r'A custom filter or module.{0,4}?such as URLScan')
    ]
    if any(i for i in schemes):
        return True
    return False