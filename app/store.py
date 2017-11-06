import json


class Store(object):
    def __init__(self, file):
        with open(file) as data:
            self.data = json.load(data)


class WeatherStore(Store):
    def get_first(self, key):
        return self.data[key][0]


class CityStore(Store):
    def get_all(self):
        return list(self.data.keys())
