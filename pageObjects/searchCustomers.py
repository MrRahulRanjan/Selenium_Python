import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchCustomer():

    textbox_Email_id="SearchEmail"
    textbox_firstName_id="SearchFirstName"
    textbox_lastName_id="SearchLastName"
    drp_month_id="SearchMonthOfBirth"
    drp_day_id="SearchDayOfBirth"
    button_Search_id="search-customers"
    text_Serch_xpath="//div[@class='search-text']"
    tableSearchResults_xpath="//div[@class='col-md-12']"
    table_xpath="//table[@id='customers-grid']"
    table_rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_column_xpath="//table[@id='customers-grid']//tbody/tr/td"



    def __init__(self, driver):
        self.driver=driver

    def enterSearchEmail(self,email):
        self.driver.find_element(By.ID, self.textbox_Email_id).clear()
        self.driver.find_element(By.ID, self.textbox_Email_id).send_keys(email)

    def enterFirstName(self,firstName):
        self.driver.find_element(By.ID, self.textbox_firstName_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstName_id).send_keys(firstName)

    def enterLastName(self,lastName):
        self.driver.find_element(By.ID, self.textbox_lastName_id).clear()
        self.driver.find_element(By.ID, self.textbox_lastName_id).send_keys(lastName)

    def selectMonth(self,value):
        drpMonth=Select(self.driver.find_element(By.ID, self.drp_month_id))
        drpMonth.select_by_value(value)

    def selectDay(self,value):
        drpDay=Select(self.driver.find_element(By.ID, self.drp_day_id))
        drpDay.select_by_value(value)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.button_Search_id).click()


    def clickSearchToggle(self):
        self.driver.find_element(By.XPATH, self.text_Serch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def searchCustomerBYEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table= self.driver.find_element(By.XPATH, self.table_xpath)
            emailId= table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailId==email:
                flag=True
                break
            return flag
    def searchCustomerBYName(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table= self.driver.find_element(By.XPATH, self.table_xpath)
            Name= table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag = True
                break
            return flag
