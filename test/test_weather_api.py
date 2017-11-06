from os.path import join, dirname

from falcon import testing

from ..app.api import create_app


class ApiTestCase(testing.TestCase):
    def setUp(self):
        super(ApiTestCase, self).setUp()

        # data.json can be replaced by other testing fixtures
        data_file = join(dirname(dirname(__file__)), 'data.json')
        self.app = testing.TestClient(create_app(data_file))

    def test_get_weather_of_valid_city_succeed(self):
        result = self.app.simulate_get('/weathers/hongkong')
        expected = {
            'temperature': {
                'value': -12,
                'measurement': 'C'
            },
            'humidity': 1,
            'wind': {
                'speed': 2,
                'degree': 115
            },
            'status': 'Sunny',
            'pressure': 1130
        }
        self.assertEqual(result.json, expected)
        self.assertEqual(result.status_code, 200)

    def test_get_weather_of_invalid_city_raise_404(self):
        """Get invalid city should raise 404 (Not Found)"""

        result = self.app.simulate_get('/weathers/random')
        self.assertEqual(result.status_code, 404)

    def test_get_invalid_path_raise_404(self):
        """Get invalid path should raise 404 (Not Found)"""

        result = self.app.simulate_get('/somerandompath')
        self.assertEqual(result.status_code, 404)

    def test_get_a_list_of_cities(self):
        """For a full list of cities, query the /cities endpoint"""

        result = self.app.simulate_get('/cities')
        cities = result.json
        self.assertTrue('hongkong' in cities)
        self.assertTrue('beijing' in cities)

    def test_post_request_raises_405(self):

        result = self.app.simulate_post('/weathers/hongkong')
        self.assertEqual(result.status_code, 405)
