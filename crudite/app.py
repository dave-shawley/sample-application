from tornado import web
import sprockets.http.app
import sprockets.handlers.status


class Application(sprockets.http.app.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__([
            web.url('/status', sprockets.handlers.status.StatusHandler),
        ], *args, **kwargs)
        sprockets.handlers.status.set_application(__package__)
