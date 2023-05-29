from configparser import ConfigParser


def readConfiguration(section, key):
    config = ConfigParser()
    config.read("./configurations/config.ini")
    return config.get(section, key)
