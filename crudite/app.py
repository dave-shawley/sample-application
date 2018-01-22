import os

from sprockets.mixins.mediatype import content, transcoders
from tornado import web
import psycopg2
import queries
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

        self.settings['database_url'] = os.environ.get(
            'PGSQL_USERS', 'postgresql://localhost/postgres')
        self.database = None
        self.before_run_callbacks.append(self.before_run)
        self.on_shutdown_callbacks.append(self.on_shutdown)

    def before_run(self, _, _io_loop):
        self.database = queries.TornadoSession(self.settings['database_url'])

    def on_shutdown(self, _):
        if self.database:
            try:
                self.database.close()
            except psycopg2.InterfaceError:
                pass  # connection not open
            self.database = None
