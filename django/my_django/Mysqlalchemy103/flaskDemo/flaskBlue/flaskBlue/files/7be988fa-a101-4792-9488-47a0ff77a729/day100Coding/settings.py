

class DEVConfig(object):
    DEBUG = True
    SECRET_KEY = "jalksdjgajh"


class ProConfig(object):
    DEBUG = False


class TestConfig(object):
    TESTING = True



# print(dir(DEVConfig))