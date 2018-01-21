import uuid

from sprockets.mixins.mediatype import content
from tornado import web
import sprockets.http.mixins


class CollectionHandler(content.ContentMixin,
                        sprockets.http.mixins.ErrorLogger,
                        sprockets.http.mixins.ErrorWriter,
                        web.RequestHandler):

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
        for user in self.application.database.values():
            if user['login'] == body['login']:
                self.send_error(409, reason='Username Exists')
                return

        user_id = str(uuid.uuid4())
        body['id'] = user_id
        self.application.database[user_id] = body
        self.redirect(self.reverse_url('entry', user_id), status=303)


class EntryHandler(content.ContentMixin, sprockets.http.mixins.ErrorLogger,
                   sprockets.http.mixins.ErrorWriter, web.RequestHandler):

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
        user = self.application.database[user_id]
        self.set_status(200)
        self.send_response(user)
