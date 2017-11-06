from os.path import join, dirname

import falcon

from .store import WeatherStore, CityStore
from .resources import WeatherResource, CityResource


def create_app(data_file):
    """Create falcon API app with routes and resources configured

    This methods is needed by functional test because a falcon API app
    instance is needed. Check out test/test_weather_api.py for more
    """

    weather_store = WeatherStore(data_file)
    weather_resource = WeatherResource(weather_store)
    city_store = CityStore(data_file)
    city_resource = CityResource(city_store)
    api = falcon.API()
    api.add_route('/weathers/{city}', weather_resource)
    api.add_route('/cities', city_resource)
    return api


def get_app():
    """Get falcon API app instance

    This is used by gunicorn to start api server
    e.g. gunicorn 'app.api:get_app()'
    """

    data_file = join(dirname(dirname(__file__)), 'data.json')
    return create_app(data_file)
