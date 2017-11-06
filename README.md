# Weather API

## URL Schema

Query `/weathers/{city}` to get current weather for `{city}`

This is the most straightforward url schema that meets the requirement without
further assumptions of additional functionality support

e.g. (from command line with `curl` installed, else you can also visit the url inside browser)

`curl -i https://fake-weather-api.herokuapp.com/weathers/hongkong`

`curl -i https://fake-weather-api.herokuapp.com/weathers/beijing`

`curl -i https://fake-weather-api.herokuapp.com/weathers/shenzhen`

`curl -i https://fake-weather-api.herokuapp.com/weathers/shanghai`

`curl -i https://fake-weather-api.herokuapp.com/weathers/tokyo`

`curl -i https://fake-weather-api.herokuapp.com/weathers/sanfrancisco`

### A sample response

```
{
  "temperature": {
      "value": -12,
      "measurement": "C"
  },
  "humidity": 1,
  "wind": {
      "speed": 2,
      "degree": 115
  },
  "status": "Sunny",
  "pressure": 1130
}
```

### Other optiosn that were considered but weren't adopted

1. `/weathers?city={name}`

This is used by https://openweathermap.org/api, which is the most flexible choice.
It supports query by city name, city postal code, or even coordinate ranges.
It is likely to be the schema I'll use in a real project. But here we only need to
query by city name

2. `/cities/{name}/weather`

This is also a flexible choice. `{name}` field could be the city's database id, or
the name. From database's perspective, city will have its own table and weather will
be another table with city as a foreign key in it.
But this schema looks like the city also has other type of resources other than weather,
while the requirement only needs weather of a city with no specification of other
type of resources. Thus this option was also not used.

### Development

```
git clone git@github.com:zzhjerry/weather-api.git
cd weather-api

# use virtualenv to manage dependencies need by ths app
# assume you have python3 isntalled
virtualenv -p python3 .env
source .env/bin/activate

# install dependencies
pip3 install -r requirements.txt

# you do need to source again to adopt newly install local gunicorn command
source .env/bin/activate

# start local server on 127.0.0.1:8000
gunicorn 'app.api:get_app()'
visit http://127.0.0.1:8000/weather/hongkong in browser

# or run tests
cd ..
python3 -m unittest weather-api.test.test_weather_api
```
