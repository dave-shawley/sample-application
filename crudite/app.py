from tornado import web
import sprockets.http.app
import sprockets.handlers.status

import crudite.handlers


class Application(sprockets.http.app.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__([
            web.url('/status', sprockets.handlers.status.StatusHandler),
            web.url('/', crudite.handlers.CollectionHandler,
                    name='collection'),
            web.url('/(?P<user_id>.*)', crudite.handlers.EntryHandler,
                    name='entry'),
        ], *args, **kwargs)
        sprockets.handlers.status.set_application(__package__)
        self.database = {}
