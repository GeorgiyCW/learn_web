import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "50e6f2357bb94de1973114609202604",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False 
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return weather

if __name__ == "__main__":
    print(weather_by_city("Moscow,Russia")) 
