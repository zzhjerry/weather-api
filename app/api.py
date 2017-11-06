from os.path import join, dirname

import falcon

from .store import WeatherStore, CityStore
from .resources import WeatherResource, CityResource


def create_app(data_file):
    weather_store = WeatherStore(data_file)
    weather_resource = WeatherResource(weather_store)
    city_store = CityStore(data_file)
    city_resource = CityResource(city_store)
    api = falcon.API()
    api.add_route('/weathers/{city}', weather_resource)
    api.add_route('/cities', city_resource)
    return api


def get_app():
    data_file = join(dirname(dirname(__file__)), 'data.json')
    return create_app(data_file)
