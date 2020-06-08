#TO read data from COnfiguration file
import configparser

def readConfigData(section,key):
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Jashan\\PycharmProjects\\EndToEnd\\ConfigurationFiles\\Config.cfg")
    return config.get(section,key)

def fetchElementLocators(section,key):
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Jashan\\PycharmProjects\\EndToEnd\\ConfigurationFiles\\Elements.cfg")
    return config.get(section, key)
