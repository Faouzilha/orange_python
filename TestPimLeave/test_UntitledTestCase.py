# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(self.base_url + "chrome://newtab/")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/aside/nav/div[2]/ul/li[3]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")
        driver.find_element(By.LINK_TEXT,"Apply").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave")
        driver.find_element_by_link_text("My Leave").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[3]/span").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[4]").click()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/header/div[2]/nav/ul/li[5]").click()
        driver.find_element(By.LINK_TEXT,"Leave List").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")
        driver.find_element(By.LINK_TEXT,"Assign Leave").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
