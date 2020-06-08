from Base import InititateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest
import openpyxl
from DataGenerate import DataGen

@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver = InititateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    #register.enter_email("abcd@gmail.com")
    driver.close()

