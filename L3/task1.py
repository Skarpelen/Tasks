from datetime import datetime
import random


def getTemperature():
    return random.randint(-30, 30)


def getCurrentDay():
    today = datetime.now()
    return today


if __name__ == '__main__':
    temperature = getTemperature()
    day = getCurrentDay().day
    month = getCurrentDay().month
    print(f'Сегодня {day}.{month}. На улице {temperature} градусов.')
