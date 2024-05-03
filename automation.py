import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class testLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://stg-sob.ids.id/auth/login")
        cls.wait = WebDriverWait(cls.driver, 10)
           
    
    def login_berhasil(self):
        print("starting valid login test")
        username_input = self.driver.find_element(By.NAME, "username")
        time.sleep(3)
        username_input.send_keys("ryobranch")
        password_input = self.driver.find_element(By.NAME, "password")
        time.sleep(3)
        password_input.send_keys("Ryo@1234")
        time.sleep(3)
        click_login = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        click_login.click()
        
        success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[@class='MuiTypography-root MuiTypography-h4 css-uytwnp']")))
        self.assertIsNotNone(success_message)
        self.assertEqual(success_message.text, "Welcome!")
        print("Valid login test completed successfully")
    
        
        
    
    def login_password_invalid(self):
        username_input = self.driver.find_element(By.NAME, "username")
        time.sleep(2)
        username_input.send_keys("ryobranch")
        password_input = self.driver.find_element(By.NAME, "password")
        time.sleep(2)
        password_input.send_keys("Ryo@1234567890")
        time.sleep(2)
        click_login = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        click_login.click()
        
        error_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='MuiAlert-message css-1xsto0d']")))
        self.assertIsNotNone(error_message)
        self.assertEqual(error_message.text, "Wrong username or password!")
    
    
    def blank_login(self):
    
        username_input = self.driver.find_element(By.NAME, "username")
        time.sleep(2)
        username_input.send_keys("")
        password_input = self.driver.find_element(By.NAME, "password")
        time.sleep(2)
        password_input.send_keys("")
        time.sleep(2)
        click_login = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        click_login.click()
        
        blank_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id=':R4alat1b36:-helper-text']")))
        self.assertIsNotNone(blank_message)
        self.assertEqual(blank_message.text, "Username cannot be empty")
        print("Blank login test completed successfully")
        
    
class dashboard(testLogin):
    def view_data(self):
        self.login_berhasil()
        time.sleep(2)
        self.driver.get("https://stg-sob.ids.id/dashboard/setorku/bulk-upload-setorku")
        time.sleep(2)
        filter = self.driver.find_element(By.XPATH, "//button[normalize-space()='FILTER']")
        filter.click()
        time.sleep(2)
        click_apply = self.driver.find_element(By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.ModelFilter.MuiBox-root.css-1xg6nuv > div.MuiStack-root.css-vrnrl8 > div > div.MuiStack-root.css-1t62lt9 > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-1m74y2w")
        time.sleep(2)
        click_apply.click()
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(5)
        
        verify_viewing_data = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#__next > div > div > div > div > div.MuiContainer-root.css-141robz > div > div > div > div.MuiBox-root.css-1k4xpm > div > div.MuiDataGrid-main.css-opb0c2 > div.MuiDataGrid-virtualScroller.css-frlfct > div > div > div:nth-child(1) > div:nth-child(1)")))
        self.assertIsNotNone(verify_viewing_data)
        self.assertEqual(verify_viewing_data.text, "1")
        print("Success displaying data")
        
    def add_data(self):
        self.login_berhasil()
        self.driver.execute_script("document.body.style.zoom='80%'")
        time.sleep(2)
        self.driver.get("https://stg-sob.ids.id/dashboard/setorku/bulk-upload-setorku")
        time.sleep(2)
        new_data = self.driver.find_element(By.XPATH, "//button[normalize-space()='ADD DATA UPLOAD']")
        new_data.click()
        time.sleep(2)
        add_new_data = self.driver.find_element(By.ID, ":r23:")
        #tambahkan user baru setiap ingin menambahkan
        add_new_data.send_keys("NEW USER1")
        time.sleep(2)
        click_submit = self.driver.find_element(By.XPATH, "//div//button[contains(text(), 'SUBMIT')]")
        click_submit.click()
        
        verify_new_data = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#__next > div > div > div > div > div.MuiContainer-root.css-141robz > div > div > div > div.MuiBox-root.css-1k4xpm > div > div.MuiDataGrid-main.css-opb0c2 > div.MuiDataGrid-virtualScroller.css-frlfct > div > div > div:nth-child(1) > div:nth-child(1)")))
        self.assertIsNotNone(verify_new_data)
        self.assertEqual(verify_new_data.text, "1")
        print("Success add data")
        
class inputDetail(dashboard):
    def detail_data(self):
        self.view_data()
        time.sleep(2)
        self.driver.get("https://stg-sob.ids.id/dashboard/setorku/bulk-upload-setorku/16424")
        time.sleep(2)
        add_detail = self.driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M19 13h-6v')]")
        add_detail.click()
        
    def merchant_id(self):
        self.detail_data()
        time.sleep(2)
        input_merchant = self.driver.find_element(By.NAME, "merchantTransactionId")
        input_merchant.send_keys("IND12345678910111213")
        
    def userCode(self):
        self.detail_data()
        time.sleep(2)
        input_usercode = self.driver.find_element(By.NAME, "userCode")
        input_usercode.send_keys("IND123456789")
    
    def userName(self):
        self.detail_data()
        time.sleep(2)
        input_usercode = self.driver.find_element(By.NAME, "userName")
        input_usercode.send_keys("INDRA MARTAYUDA")
        
    def customerID(self):
        self.detail_data()
        time.sleep(2)
        input_customerid = self.driver.find_element(By.NAME, "customerId")
        input_customerid.send_keys("00011122233311122299")
        
    def totalAmount1(self):
        self.detail_data()
        time.sleep(2)
        input_total1 = self.driver.find_element(By.NAME, "totalAmount")
        input_total1.send_keys("3.000.000.00")
        time.sleep(2)
        elemen_penting =self.driver.find_element(By.NAME, "totalAmount")
        self.driver.execute_script("arguments[0].scrollIntoView();", elemen_penting)
        self.driver.save_screenshot("screenshot1.png")
    
    def totalAmount2(self):
        self.detail_data()
        time.sleep(2)
        input_total1 = self.driver.find_element(By.NAME, "totalAmount")
        input_total1.send_keys("300000000")
        time.sleep(2)
        elemen_penting =self.driver.find_element(By.NAME, "totalAmount")
        self.driver.execute_script("arguments[0].scrollIntoView();", elemen_penting)
        self.driver.save_screenshot("screenshot2.png")
        
    def period(self):
        self.detail_data()
        time.sleep(2)
        input_period = self.driver.find_element(By.NAME, "period")
        input_period.send_keys("12")    
     
         
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()
    
