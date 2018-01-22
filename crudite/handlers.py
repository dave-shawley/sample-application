from sprockets.mixins.mediatype import content
from tornado import gen, web
import psycopg2
import sprockets.http.mixins


class CollectionHandler(content.ContentMixin,
                        sprockets.http.mixins.ErrorLogger,
                        sprockets.http.mixins.ErrorWriter,
                        web.RequestHandler):

    @gen.coroutine
    def post(self):
        """
        Add a new user record.

        :reqjson string login: login name to add.
        :reqjson string first_name: user's first name (given name).
        :reqjson string last_name: user's last name (surname).
        :reqjson string email: user's email address.
        :reqjson string password: password assigned to the user.

        :status 303: the record was added and the :http:header:`Location`
            header in the response is the canonical URL
        :status 409: if the user name is already in use

        """
        body = self.get_request_body()
        try:
            results = yield self.application.database.query(
                'INSERT INTO users(login, first_name, last_name,'
                '                  email, password)'
                '         VALUES (%(login)s, %(first_name)s, %(last_name)s,'
                '                 %(email)s, %(password)s)'
                '       RETURNING id',
                body)
        except psycopg2.IntegrityError:
            self.send_error(409, reason='Username Exists')
            return
        user_id = results.as_dict()['id']
        results.free()
        self.redirect(self.reverse_url('entry', user_id), status=303)


class EntryHandler(content.ContentMixin, sprockets.http.mixins.ErrorLogger,
                   sprockets.http.mixins.ErrorWriter, web.RequestHandler):

    @gen.coroutine
    def get(self, user_id):
        """
        Fetch a user record by assigned identifier.

        :resjson string login: login name to add.
        :resjson string first_name: user's first name (given name).
        :resjson string last_name: user's last name (surname).
        :resjson string email: user's email address.

        :status 200: the user record exists and is returned in the payload
        :status 404: the requested user does not exist

        """
        results = yield self.application.database.query(
            'SELECT id, login, first_name, last_name, email, password'
            '  FROM users'
            ' WHERE id = %(user_id)s',
            {'user_id': user_id})
        user_info = results.as_dict()
        results.free()
        self.set_status(200)
        self.send_response(user_info)
