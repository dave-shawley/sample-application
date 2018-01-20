import json

from tornado import testing

import crudite.app


class StatusTests(testing.AsyncHTTPTestCase):

    def get_app(self):
        return crudite.app.Application()

    def test_that_status_returns_json(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.headers['Content-Type'],
                         'application/json; charset=UTF-8')

    def test_that_package_name_is_returned(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        body = json.loads(response.body.decode('utf-8'))
        self.assertEqual(body['application'], 'crudite')

    def test_that_version_is_returned(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        body = json.loads(response.body.decode('utf-8'))
        self.assertEqual(body['version'], crudite.version)

    def test_that_status_is_returned(self):
        response = self.fetch('/status')
        self.assertEqual(response.code, 200)
        body = json.loads(response.body.decode('utf-8'))
        self.assertEqual(body['status'], 'ok')
