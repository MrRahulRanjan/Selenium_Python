import time

import pytest
import pytest_metadata
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtilities

class Test_002_DDTLogin:
    baseURL= ReadConfig.getApplicationURL()

    path=".//TestData//LoginData.xlsx"


    logger=LogGen.logGen()


        

    @pytest.mark.regression
    def test_ddt_login(self,setup):
        self.logger.info("*********Test_001_Login**********")
        self.logger.info("*********Verifying test_login info**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows= excelUtilities.getRowCount(self.path,'Sheet2')
        print("No of rows.....",self.rows)
        lst_status=[]#empty list variable



        for r in range(2,self.rows+1):
            self.user=excelUtilities.readData(self.path,"Sheet2",r,1)
            self.password=excelUtilities.readData(self.path,"Sheet2", r,2)
            self.exp = excelUtilities.readData(self.path, "Sheet2", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Passed**")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***Failed**")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Failed**")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***Passed**")

                    lst_status.append("Passed")

        if "Fail" not in lst_status:
            self.logger.info("---Login DDT is passed-----")
            self.driver.close()
            assert True
        else:
            self.logger.info("---Login DDT is passed-----")
            self.driver.close()
            assert False

        self.logger.info("***end of test****")
        self.logger.info("----Test Completed-----")