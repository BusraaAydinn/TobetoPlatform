from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
import openpyxl
from constants import globalConstants as c

#Test senaryosu 3:  Şifresini unutan kullanıcının şifresini yenileyebilme işlemi test edilecektir.

class Test_Tobeto_Platform_Password_Reset_Test:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.SIGN_UP_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
    
    def test_successful_password_reset(self):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SIGN_UP_MAIL_XPATH)))
        emailInput.send_keys("test456@hotmail.com")
        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SEND_BUTTON_XPATH)))
        sendButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SYSTEM_MESSAGE_XPATH)))
        assert "Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin" in systemMessage.text 

    def test_unsuccessful_password_reset(self):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SIGN_UP_MAIL_XPATH)))
        emailInput.send_keys("@hotmail.com")
        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SEND_BUTTON_XPATH)))
        sendButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.ERROR_SYSTEM_MESSAGE_XPATH)))
        assert "Girdiğiniz e-posta geçersizdir" in systemMessage.text 