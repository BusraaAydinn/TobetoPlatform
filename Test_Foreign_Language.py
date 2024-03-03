from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest
import json
import openpyxl
from constants import globalConstants as c
from Valid_Login import Test_Valid_Login
from selenium.webdriver.support.select import Select

class Test_Foreign_Language:

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def webdriver_wait(self,sure,element):

        element = WebDriverWait(self.driver,sure).until(ec.visibility_of_element_located((By.CSS_SELECTOR,element)))
        return element   
    
    def read_language_data_from_json():

        file = open("language_data_from.json") 
        data = json.load(file)
        parameter = []

        for user in data['data']:
            language = user["language"]
            level = user["level"]
            
            parameter.append((language,level))

        return parameter
    
    @pytest.mark.parametrize("language,level",read_language_data_from_json())

    def test_foreign_language_successful_register(self,language,level):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)

        beginButton = self.webdriver_wait(10,c.BEGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", beginButton) 
        sleep(3)
        beginButton.click()
        sleep(2)

        foreignLanguageLink = self.webdriver_wait(10,c.FOREIGN_LANGUAGE_LINK)
        foreignLanguageLink.click()
        sleep(2)
        
        selectLanguageDropdown = self.webdriver_wait(10,c.SELECT_LANGUAGE_DROPDOWN)
        selectLanguage = Select(selectLanguageDropdown)
        selectLanguage.select_by_visible_text(language)

        selectLevelDropdown = self.webdriver_wait(20,c.SELECT_LEVEL_DROPDOWN)
        selectLevel = Select(selectLevelDropdown)
        selectLevel.select_by_visible_text(level)

        saveButton= self.webdriver_wait(20,c.SAVE_BUTTON_CSS)
        saveButton.click()

        expectedResult = self.webdriver_wait(20,c.EXPECTED_RESULT_CSS)
        actualResult = "• Yabancı dil bilgisi eklendi."
        assert expectedResult.text == actualResult

    def test_delete_added_language(self):  
        
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)
        
        beginButton = self.webdriver_wait(10,c.BEGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", beginButton) 
        sleep(3)
        beginButton.click()
        sleep(2)

        foreignLanguageLink = self.webdriver_wait(10,c.FOREIGN_LANGUAGE_LINK)
        foreignLanguageLink.click()
        sleep(2)

        firstRegisteredLanguage = self.webdriver_wait(20,c.REGISTERED_LANGUAGES_1)
        firstRegisteredLanguage.click()

        trashBin = self.webdriver_wait(20,c.DELETE_ICON)
        trashBin.click()
        sleep(2)

        noButton = self.webdriver_wait(10,c.NO_BUTTON)
        noButton.click()

        languageVisibilityController = self.webdriver_wait(20,c.REGISTERED_LANGUAGES_1)
        result = languageVisibilityController.is_displayed()
        
        assert result == True
        firstRegisteredLanguage = self.webdriver_wait(20,c.REGISTERED_LANGUAGES_1)
        firstRegisteredLanguage.click()

        trashBin = self.webdriver_wait(20,c.DELETE_ICON)
        trashBin.click()
        
        yesButton = self.webdriver_wait(10,c.YES_BUTTON)
        yesButton.click()

        expectedResult = self.webdriver_wait(20,c.EXPECTED_RESULT_CSS)
        assert expectedResult.text == "• Yabancı dil kaldırıldı."

    def test_foreign_language_unsuccessful_register(self):
        
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)

        beginButton = self.webdriver_wait(10,c.BEGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", beginButton) 
        sleep(3)
        beginButton.click()
        sleep(2)

        foreignLanguageLink = self.webdriver_wait(10,c.FOREIGN_LANGUAGE_LINK)
        foreignLanguageLink.click()
        sleep(2)

        saveButton= self.webdriver_wait(20,c.SAVE_BUTTON_CSS)
        saveButton.click()

        requiredFieldLanguage = self.webdriver_wait(10,c.REQUIRED_FIELD_LANGUAGE)
        requiredFieldLevel = self.webdriver_wait(10,c.REQUIRED_FIELD_LEVEL)
        assert requiredFieldLanguage.text == "Doldurulması zorunlu alan*"
        assert requiredFieldLevel.text == "Doldurulması zorunlu alan*"
        sleep(3)
            