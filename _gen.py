########################################
# This file generates weather fixtures #
########################################

import random
import json
from enum import Enum


class WeatherStatus(Enum):
    PARTLY_CLOUDY = 'Partly cloudy'
    LIGHT_RAIN = 'Light rain'
    THUNDERSTORM = 'Thunderstorm'
    SUNNY = 'Sunny'


def generate_weater():
    weather = {
        'temperature': {
            'value': random.randrange(-20, 40),
            'measurement': 'C'
        },
        'humidity': random.randrange(0, 100),
        'wind': {
            'speed': random.randrange(0, 10),
            'degree': random.randrange(0, 360)
        },
        'status': random.choice(list(WeatherStatus)).value,
        'pressure': random.randrange(900, 1200)
    }
    return weather


def main():
    cities = [
        'hongkong', 'shenzhen', 'beijing', 'shanghai',
        'tokyo', 'london', 'sanfrancisco', 'jakarta',
        'berlin', 'paris'
    ]
    data = {}
    for city in cities:
        data[city] = [generate_weater(), generate_weater()]
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    main()
