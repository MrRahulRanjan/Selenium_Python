import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer():
    link_customers_xpath= "//a[@href='#']//p[contains(text(),'Customers')]"
    link_subCustomer_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_addNew_xpath="//a[normalize-space()='Add new']"
    textbox_email_id="Email"
    textbox_password_id="Password"
    textbox_firstName_id= "FirstName"
    textbox_lastName_id= "LastName"
    rdMale_id="Gender_Male"
    rdFemale_id= "Gender_Female"
    textbox_DOB_id="DateOfBirth"
    textbox_companyName_id="Company"
    checkbox_Istaxexempt_id= "IsTaxExempt"
    textbox_CustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listItem_Administrator_xpath="//li[contains(text(),'Administrators')]"
    listItem_Registered_xpath="//li[contains(text(),'Registered')]"
    listItem_Guest_xpath="//li[contains(text(),'Guests')]"
    listItem_Vendor_xpath="//li[contains(text(),'Vendors')]"
    drp_mngrOfVendor_id="VendorId"
    checkbox_Active_id="Active"
    textbox_adminComment_id= "AdminComment"
    button_save_name="save"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_customers_xpath).click()

    def clickCustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.link_subCustomer_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.button_addNew_xpath).click()

    def enterMailId(self,email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def enterPasword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def enterFirstName(self,firstName):
        self.driver.find_element(By.ID, self.textbox_firstName_id).send_keys(firstName)

    def enterLastName(self,lastName):
        self.driver.find_element(By.ID, self.textbox_lastName_id).send_keys(lastName)

    def clickGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID, self.rdMale_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID, self.rdFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMale_id).click()

    def enterDOB(self,DOB):
        self.driver.find_element(By.ID, self.textbox_DOB_id).send_keys(DOB)

    def enterCompanyName(self,companyName):
        self.driver.find_element(By.ID, self.textbox_companyName_id).send_keys(companyName)

    def clickTaxEtempt(self):
        self.driver.find_element(By.ID, self.checkbox_Istaxexempt_id).click()

    def clickCustomerRole(self,role):
        self.driver.find_element(By.XPATH, self.textbox_CustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listItem=self.driver.find_element(By.XPATH, self.listItem_Registered_xpath)
        elif role=="Administrators":
            self.listItem=self.driver.find_element(By.XPATH, self.listItem_Administrator_xpath)

        elif role=="Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listItem=self.driver.find_element(By.XPATH, self.listItem_Guest_xpath)
        elif role=="Registered":
            self.listItem = self.driver.find_element(By.XPATH, self.listItem_Registered_xpath)
        elif role == "Vendors":
            self.listItem=self.driver.find_element(By.XPATH, self.listItem_Vendor_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.listItem_Guest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def managerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.ID, self.drp_mngrOfVendor_id))
        drp.select_by_visible_text(value)

    def clickActive(self):
        self.driver.find_element(By.ID, self.checkbox_Active_id).click()

    def enterAdminComment(self,comment):
        self.driver.find_element(By.ID, self.textbox_adminComment_id).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.NAME, self.button_save_name).click()




