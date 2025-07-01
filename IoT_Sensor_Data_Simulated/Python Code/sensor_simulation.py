import random

def get_sensor_data():
    temperature = round(random.uniform(20, 40), 2)
    humidity = round(random.uniform(30, 70), 2)
    gas_level = round(random.uniform(200, 800), 2)
    return temperature, humidity, gas_level
