import json
import uuid

from tornado import testing
import faker

import crudite.app


class CreateEndpointTests(testing.AsyncHTTPTestCase):

    @classmethod
    def setUpClass(cls):
        super(CreateEndpointTests, cls).setUpClass()
        cls.fakes = faker.Factory.create()

    def setUp(self):
        self.application = None
        super(CreateEndpointTests, self).setUp()
        self.request = {'login': str(uuid.uuid4()),
                        'first_name': self.fakes.first_name(),
                        'last_name': self.fakes.last_name(),
                        'email': self.fakes.safe_email(),
                        'password': self.fakes.password()}

    def tearDown(self):
        super(CreateEndpointTests, self).tearDown()
        self.application.on_shutdown(self.application)

    def get_app(self):
        self.application = crudite.app.Application()
        self.io_loop.add_callback(self.application.before_run,
                                  self, self.io_loop)
        return self.application

    def test_that_create_endpoint_redirects_to_entry_handler(self):
        response = self.fetch('/', method='POST', follow_redirects=False,
                              body=json.dumps(self.request).encode('utf-8'),
                              headers={'Content-Type': 'application/json'})
        self.assertEqual(response.code, 303)
        url = response.headers['Location']
        self.assertTrue(
            url.startswith(self.application.reverse_url('entry', '')))

    def test_that_create_endpoint_returns_new_identifier(self):
        response = self.fetch('/', method='POST',
                              body=json.dumps(self.request).encode('utf-8'),
                              headers={'Content-Type': 'application/json',
                                       'Accept': 'application/json'})
        self.assertEqual(response.code, 200)
        self.assertEqual(response.headers['Content-Type'],
                         'application/json; charset="utf-8"')
        body = json.loads(response.body.decode('utf-8'))
        self.assertIn('id', body)
        self.assertIn(body['id'], response.effective_url)

    def test_that_create_endpoint_returns_all_data(self):
        response = self.fetch('/', method='POST',
                              body=json.dumps(self.request).encode('utf-8'),
                              headers={'Content-Type': 'application/json',
                                       'Accept': 'application/json'})
        self.assertEqual(response.code, 200)
        self.assertEqual(response.headers['Content-Type'],
                         'application/json; charset="utf-8"')
        body = json.loads(response.body.decode('utf-8'))
        body.pop('id')
        self.assertEqual(body, self.request)

    def test_that_creating_two_users_with_same_login_fails(self):
        response = self.fetch('/', method='POST',
                              body=json.dumps(self.request).encode('utf-8'),
                              headers={'Content-Type': 'application/json'})
        self.assertEqual(response.code, 200)

        next_request = {'login': self.request['login'],
                        'first_name': self.fakes.first_name(),
                        'last_name': self.fakes.last_name(),
                        'email': self.fakes.safe_email(),
                        'password': self.fakes.password()}
        response = self.fetch('/', method='POST',
                              body=json.dumps(next_request).encode('utf-8'),
                              headers={'Content-Type': 'application/json'})
        self.assertEqual(response.code, 409)
