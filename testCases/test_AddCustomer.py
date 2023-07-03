import random
import string

import pytest
import pytest_metadata
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from pageObjects.addCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()
    logger=LogGen.logGen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_addCustomer(self,setup):
        self.logger.info("******Test_003_AddCustomer*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******Login_Successfull*****")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickCustomerSubMenu()

        self.addcust.clickOnAddNew()

        self.logger.info("******Providing_Customer_info*****")

        self.email=random_generator()+ "@gmail.com"
        self.addcust.enterMailId(self.email)
        self.addcust.enterPasword("rahul30799")
        self.addcust.enterFirstName("Rahul")
        self.addcust.enterLastName("Ranjan")
        self.addcust.enterDOB("12/2/1992")
        self.addcust.enterAdminComment("Hello This is my first id")
        self.addcust.enterCompanyName("Rahul KI Company")
        self.addcust.clickGender("Male")
        self.addcust.clickCustomerRole("Guests")
        self.addcust.managerOfVendor("Vendor 2")
        self.addcust.clickTaxEtempt()
        self.addcust.clickSave()

        self.logger.info("******Saving_Customer_Info**********")

        self.logger.info("******Add_Customer_Validation_Started**********")

        self.msg= self.driver.find_element(By.TAG_NAME,"body").text
        self.driver.quit()
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("******Add_Customer_Test_Passed**********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_add_customer.png")
            self.logger.info("******Add_Customer_Test_Failed**********")
            assert True==False

        self.logger.info("******Ending Test Case 003**********")




def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for x in range(size))

