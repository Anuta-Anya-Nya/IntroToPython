# пользовательский интерфейс (UI)
import data_provider as prov
import logger as log


def temperature_viev(sensor):
    data = prov.get_temprature(sensor)
    log.temperature_logger(data)
    return data


def pressure_viev(sensor):
    data = prov.get_preassure(sensor)
    log.presser_logger(data)
    return data


def wind_speed_viev(sensor):
    data = prov.get_wind_speed(sensor)
    log.wind_speed_logger(data)
    return data
