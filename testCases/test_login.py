import pytest
import pytest_metadata
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()

    logger=LogGen.logGen()


    @pytest.mark.regression

    def test_homePageTitle(self,setup):
        self.logger.info("*********Test_001_Login**********")
        self.logger.info("*********Verifying Home Page Title**********")
        self.driver =setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        print(act_title)
        if act_title=="Your store. Login":
            self.driver.close()
            self.logger.info("*********Verifying Home Page Title is passed**********")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********Verifying Home Page Title Passed**********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*********Test_001_Login**********")
        self.logger.info("*********Verifying test_login info**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title=self.driver.title
        self.lp.clickLogout()


        if act_title=="Dashboard / nopCommerce administration":
            assert True#print("Pass")
            self.logger.info("*********Verifying test_login is Passed**********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_login.png")
            self.driver.close()
            self.logger.warn("*********Verifying test_login is Failed**********")
            assert False#print("Fail")
