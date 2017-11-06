import json

import falcon


class Resource(object):
    def __init__(self, store):
        self.data = store


class WeatherResource(Resource):
    def on_get(self, req, res, city):
        try:
            res.body = json.dumps(self.data.get_first(city))
        except KeyError:
            raise falcon.HTTPNotFound()


class CityResource(Resource):
    def on_get(self, req, res):
        res.body = json.dumps(self.data.get_all())
