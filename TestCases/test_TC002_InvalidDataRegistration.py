from Base import InititateDriver
from Library import ConfigReader

def test_registrationInvalidData():
    driver = InititateDriver.startBrowser()
    driver.close()

