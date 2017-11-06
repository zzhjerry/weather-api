import json

import falcon


class Resource(object):
    """Inherited by different Resource subclasses"""

    def __init__(self, store):
        self.data = store


class WeatherResource(Resource):
    """Weather resource constructor, used by /weathers/{city} route"""

    def on_get(self, req, res, city):
        """Called when get request is received"""

        try:
            res.body = json.dumps(self.data.get_first(city))
        except KeyError:
            raise falcon.HTTPNotFound()


class CityResource(Resource):
    """City Resource constructor, used by /cities route

    Use mainly as a helper to get available cities
    """

    def on_get(self, req, res):
        """Called when get request is received"""

        res.body = json.dumps(self.data.get_all())
