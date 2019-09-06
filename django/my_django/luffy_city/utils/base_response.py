class BaseResponse(object):
    def __init__(self):
        self.code = 1000
        self.error = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__

# res = BaseResponse()
# res.code = 1001
# res.error = "xxxx"
# res.dict
