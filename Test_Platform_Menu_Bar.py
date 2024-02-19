from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
from constants import globalConstants as c


class Test_Platform_Menu_Bar:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()    
  
    @pytest.mark.parametrize("Email, Password", [("dojogij877@wikfee.com", "deneme123")])
    def test_menu_bar_ikon(self,Email,Password):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        emailInput.send_keys(Email)
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        passwordInput.send_keys(Password)
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        loginButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH, c.SYSTEM_SUCCESSFUL_MESSAGE_XPATH)))
        assert systemMessage.text == "• Giriş başarılı." 
            
        homePageButton = self.driver.find_element(By.XPATH, c.HOME_PAGE)
        homePageButton.click()
        sleep(2)

        homePageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.HOME_PAGE_CONTROLLER)))
        assert homePageController.text == "TOBETO'ya hoş geldin"
        sleep(3)
            
        myProfileButton = self.driver.find_element(By.XPATH, c.MY_PROFILE)
        myProfileButton.click()
        sleep(3)

        profileController = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.MY_PROFILE_CONTROLLER)))
        assert profileController.text == "Buse Arslan"
        sleep(3)

        assessmentsButton = self.driver.find_element(By.XPATH, c.ASSESSMENTS)
        assessmentsButton.click()
        sleep(3)

        assessmentsController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.ASSESSMENTS_CONTROLLER)))
        assert assessmentsController.text == "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
        sleep(3)

        catalogButton = self.driver.find_element(By.XPATH, c.CATALOG)
        catalogButton.click()
        sleep(3)

        catalogController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.CATALOG_CONTROLLER)))
        assert catalogController.text == "Öğrenmeye başla !"
        sleep(3)

        calendarButton = self.driver.find_element(By.XPATH, c.CALENDAR)
        calendarButton.click()
        sleep(3)

        calendarController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.CALENDAR_CONTROLLER)))
        assert calendarController.text == "Bugün"
        sleep(3)
            
        istanbulCodingButton = self.driver.find_element(By.XPATH, c.ISTANBUL_CODING)
        istanbulCodingButton.click()
        sleep(3)

        istanbulCodingController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.ISTANBUL_CODING_CONTROLLER)))
        assert istanbulCodingController.text == "Aradığın  “İş”  Burada!"
        sleep(3)