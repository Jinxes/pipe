from flask.views import View

class Controller(View):

    methods = ['GET']

    def dispatch_request(self):
        return 'Hello World'
