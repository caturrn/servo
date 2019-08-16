#server program


import requests
import json
import paho.mqtt.client as mqtt

weatherprovider = mqtt.Client()
broker_url = "127.0.0.1"
broker_port = 1883

while True:
    latitude = '-7.7653071'
    lon = '110.3723343'
    api = '5d99b8d27c505b0337b2f5fd568ec7c4'
    weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={lon}&units=metric&APPID={api}')
    weatherdic = json.loads(weather.content)
    weathermain = (weatherdic["weather"])
    weathercond=(weathermain[0]['main'])
    client.connect(broker_url, broker_port)
    client.publish(topic="weather", payload= weathercond, qos=1, retain=False)
    client.disconnect()
    time.sleep(15)

