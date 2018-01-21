from sprockets.mixins.mediatype import content, transcoders
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
        content.add_transcoder(self, transcoders.JSONTranscoder())
        content.set_default_content_type(self, 'application/json',
                                         encoding='utf-8')

        self.database = {}
