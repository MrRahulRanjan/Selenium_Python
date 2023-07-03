import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomer import AddCustomer
from pageObjects.searchCustomers import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.regrassion
class Test_004_SearchCustomer:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()
    logger=LogGen.logGen()

    @pytest.mark.regrassion

    def test_searchCustomer(self,setup):
        self.logger.info("******Test_004_Search_Customer*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login_Successfull*****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickCustomerSubMenu()
        self.logger.info("******Moved_To_SearchBar*****")

        self.srchcust= SearchCustomer(self.driver)
        self.srchcust.enterSearchEmail("james_pan@nopCommerce.com")
        #self.srchcust.enterFirstName("James")
        #self.srchcust.enterLastName("Ranjan")
        #self.srchcust.selectDay("2")
        #self.srchcust.selectMonth("12")
        self.srchcust.clickSearch()

        time.sleep(5)
        #status=self.srchcust.searchCustomerBYName("James")
        status1=self.srchcust.searchCustomerBYEmail("james_pan@nopCommerce.com")
        assert True == status1


        self.logger.info("******Text Completed*****")



        self.driver.quit()




