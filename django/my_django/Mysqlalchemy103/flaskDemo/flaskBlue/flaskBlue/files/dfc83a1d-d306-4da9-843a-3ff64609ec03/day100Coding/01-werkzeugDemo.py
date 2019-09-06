from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


@Request.application
def run(request):
    return Response("王佳豪~~~")



# def run(envrion, start_responst):
#     .....
#     return [b"xxxx"]


if __name__ == '__main__':
    run_simple('localhost', 5000, run)