from nose_tests.constants import EMINEM
from nose_tests.nd_test_case import NDTestCase
from flask_app import app


class DiscussionAPITest(NDTestCase):

    def setUp(self):
        super(DiscussionAPITest, self).setUp()

    def test_get(self):
        uri = '{}/artists/{}/discussions'.format(app.config['BASE_URL'], EMINEM)
        response = self.json_get(uri)

        self.assertEqual(response.status_code, app.config['NOT_FOUND'])

        payload = {
            'discussion': 'Bust that crazy shit!'
        }
        response = self.json_post(uri, payload, data_json=True)
        self.assertEqual(response.status_code, app.config['OK'])
        reponse_dict = self.dict_from_response(response)