from selenium import webdriver


import  pytest
from selenium import webdriver

from selenium.webdriver.support.events import EventFiringWebDriver



@pytest.fixture()

def setup(browser):
    if browser=='chrome':

        options= webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver=webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        print("Launching chrome browser......")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching firefox browser......")
    else:
        driver=webdriver.Ie()

    #request.cls.driver=driver
    return driver

def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture() #this will return the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")

'''*************PyTest HTML Report***********'''

#It id hook for adding  Environment info to HTML Report

'''def pytest_configure(config):
        config._metadata['Project Name']= 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Rahul'

# It is hook for delete/modify  Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)'''

