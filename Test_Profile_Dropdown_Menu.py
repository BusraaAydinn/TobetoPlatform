import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Valid_Login import Test_Valid_Login

class Test_Profile_Dropdown_Menu:

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()    

    def test_successful_profile_information_entry(self):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("busraaaydinn67@gmail.com","*******")
        sleep(3)  
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)

        profileInformationButton = self.driver.find_element(By.XPATH, c.PROFILE_INFORMATION_BUTTON)
        profileInformationButton.click()
        sleep(4)
        
        birthdayInput = self.driver.find_element(By.NAME, c.BIRTHDAY_INPUT)
        birthdayInput.send_keys("**-**-****")  

        identityNumber =self.driver.find_element(By.NAME, c.IDENTITY_NUMBER)
        identityNumber.send_keys("***********")
       
        countryName = self.driver.find_element(By.NAME, c.COUNTRY_NAME)
        countryName.send_keys("Türkiye")
        sleep(4)

        self.driver.execute_script("window.scrollTo(0,1000)")

        city = WebDriverWait(self.driver,25).until(ec.element_to_be_clickable((By.NAME, c.CITY)))
        city.click()
        sleep(3)

        cityName = self.driver.find_element(By.XPATH, c.CITY_NAME)
        cityName.click()
        sleep(3) 

        district = self.driver.find_element(By.NAME, c.DISTRICT)
        district.click()

        districtName = self.driver.find_element(By.XPATH, c.DISTRICT_NAME)
        districtName.click()
        sleep(3)

        enterAddress = self.driver.find_element(By.NAME, c.ADDRESS)
        enterAddress.send_keys("*****")
        sleep(2)
            
        aboutMe = self.driver.find_element(By.XPATH, c.ABOUT_ME)
        aboutMe.send_keys("Kendimi geliştiriyorum, yazılım testi yapmak en büyük hobim")
        sleep(3)

        saveButton = self.driver.find_element(By.XPATH, c.SAVE_BUTTON)
        saveButton.click()
        sleep(3)

        messageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CLASS_NAME, c.MESSAGE)))
        assert messageController.text == "• Bilgileriniz başarıyla güncellendi." 
        sleep(5)

    def test_unsuccessful_profile_information_entry(self):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3) 
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)

        profileInformationButton = self.driver.find_element(By.XPATH, c.PROFILE_INFORMATION_BUTTON)
        profileInformationButton.click()
        sleep(4)
        
        birthdayInput = self.driver.find_element(By.NAME, c.BIRTHDAY_INPUT)
        birthdayInput.send_keys("**-**-****")  

        identityNumber =self.driver.find_element(By.NAME, c.IDENTITY_NUMBER)
        identityNumber.send_keys("***********")
       
        countryName = self.driver.find_element(By.NAME, c.COUNTRY_NAME)
        countryName.send_keys("Türkiye")

        self.driver.execute_script("window.scrollTo(0,700)")

        city = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.NAME, c.CITY)))
        sleep(3)
        city.click()

        cityName = self.driver.find_element(By.XPATH, c.CITY_NAME)
        cityName.click()
        sleep(3)

        district = self.driver.find_element(By.NAME, c.DISTRICT)
        district.click()

        districtName = self.driver.find_element(By.XPATH, c.DISTRICT_NAME)
        districtName.click()
        sleep(3)

        saveButton = self.driver.find_element(By.XPATH, c.SAVE_BUTTON)
        sleep(3)
        saveButton.click()
        sleep(3)

        errorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CLASS_NAME, c.ERROR_MESSAGE_CONTROLLER)))
        assert errorMessageController.text == "• Kimlik bilgilerinizi hatalı girdiniz."
        sleep(3)    

    def test_empty_profile_information_entry(self, actualResult = "Doldurulması zorunlu alan*"):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3) 
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)

        profileInformationButton = self.driver.find_element(By.XPATH, c.PROFILE_INFORMATION_BUTTON)
        profileInformationButton.click()
        sleep(4)

        enterName = self.driver.find_element(By.NAME, c.NAME)
        enterName.clear()

        enterSurname = self.driver.find_element(By.NAME, c.SURNAME)
        enterSurname.clear()
        
        birthdayInput = self.driver.find_element(By.NAME, c.BIRTHDAY_INPUT)
        birthdayInput.send_keys("")  

        identityNumber =self.driver.find_element(By.NAME, c.IDENTITY_NUMBER)
        identityNumber.send_keys("")
       
        countryName = self.driver.find_element(By.NAME, c.COUNTRY_NAME)
        countryName.send_keys("")

        self.driver.execute_script("window.scrollTo(0,1200)")
        sleep(7)

        saveButton = self.driver.find_element(By.XPATH, c.SAVE_BUTTON)
        sleep(3)
        saveButton.click()
        sleep(3)

        expectedResult = WebDriverWait(self.driver,20).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR,c.ERROR_MESSAGE_EMPTY_PROFILE)))
        sleep(1)
        for i in range (len(expectedResult)):
            result = expectedResult[i]
            if result.text == "Aboneliklerde fatura için doldurulması zorunlu alan" or "*Aboneliklerde fatura için doldurulması zorunlu alan":
                continue
            else: 
                assert result.text == actualResult

    def test_logout(self):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3) 
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)  

        logoutButton = self.driver.find_element(By.XPATH, c.LOGOUT_BUTTON)  
        logoutButton.click()
        sleep(2)

        logoutController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.LOGOUT_CONTROLLER)))
        sleep (5)
        assert logoutController.text == "Giriş Yap"








        








    