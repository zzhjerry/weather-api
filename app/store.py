import json


class Store(object):
    """Inherited by different Store subclasses

    Take a json data file and load it as raw data value
    for other methods to operate on.
    """

    def __init__(self, file):
        with open(file) as data:
            self.data = json.load(data)


class WeatherStore(Store):
    """Defines how to get weather data"""

    def get_first(self, key):
        """Get the first weather record from weather list

        Each city has a list of historical weathers. The first one
        is the current weather that api reports

        :param key: city's name
        :return weather object
        :rtype object
        :raise KeyError: handled by WeatherResource which respond 404 not found
        """
        return self.data[key][0]


class CityStore(Store):
    """Defines how to get city data"""

    def get_all(self):
        """Get all cities in as a list"""

        return list(self.data.keys())
