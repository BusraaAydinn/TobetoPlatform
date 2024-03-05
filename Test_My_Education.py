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
from selenium.webdriver.chrome.service import Service

class Test_My_Education:

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def webdriver_wait(self,sure,element):

        element = WebDriverWait(self.driver,sure).until(ec.visibility_of_element_located((By.CSS_SELECTOR,element)))
        return element   
    
    def read_successful_education_data_json():

        file = open("successful_education_data.json") 
        data = json.load(file)
        parameter = []

        for user in data['data']:
            education_level = user["education_level"]
            school = user["school"]
            department = user["department"]
            start_year = user["start_year"]
            graduation_year = user["graduation_year"]

            parameter.append((education_level,school,department,start_year,graduation_year))

        return parameter
    
    def read_continue_education_data_json():

        file = open("continue_education_data.json") 
        data = json.load(file)
        parameter = []

        for user in data['data']:
            education_level = user["education_level"]
            school = user["school"]
            department = user["department"]
            start_year = user["start_year"]

            parameter.append((education_level,school,department,start_year))

        return parameter
    
    @pytest.mark.parametrize("education_level,school,department,start_year,graduation_year",read_successful_education_data_json())
    def test_my_education_successful_register(self,education_level,school,department,start_year,graduation_year,actualResult = "• Eğitim bilgisi eklendi."):
        
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)

        beginButton = self.webdriver_wait(10,c.BEGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", beginButton) 
        sleep(3)
        beginButton.click()
        sleep(2)

        myEducationLink = self.webdriver_wait(10,c.MY_EDUCATION_LINK)
        myEducationLink.click()

        selectEducationDropdown = self.webdriver_wait(10,c.SELECT_EDUCATION_DROPDOWN)
        selectEducation = Select(selectEducationDropdown)
      
        selectEducation.select_by_visible_text(education_level)
       
        enterUniversity =self.webdriver_wait(10,c.ENTER_UNIVERSITY)
        enterUniversity.send_keys(school)
        
        deparmentName = self.webdriver_wait(10,c.DEPARTMENT_NAME)
        deparmentName.send_keys(department)

        graduation_year = self.webdriver_wait(10,c.GRADUATION_YEAR)
        assert graduation_year.is_enabled() == False 

        beginDate =self.webdriver_wait(30,c.BEGIN_DATE)
        beginDate.send_keys(start_year)
        assert graduation_year.is_enabled() == True
        graduation_year.click()

        selectDateCalendar = self.webdriver_wait(10,c.SELECT_DATE_CALENDAR)
        selectDateCalendar.click()
        
        continueEducation = self.webdriver_wait(10,c.CONTINUE_CSS)
        assert continueEducation.is_enabled() == False 
        #burada bug var, 'devam ediyorum' onay kutusu aktif olmamalı

        saveButton = self.webdriver_wait(20,c.SAVE_BUTTON_CSS)
        saveButton.click()

        expectedResult = self.webdriver_wait(10,c.EXPECTED_RESULT_CSS)
        assert expectedResult.text == actualResult
        sleep(3)

    @pytest.mark.parametrize("education_level,school,department,start_year",read_continue_education_data_json())
    def test_continue_with_select_registration(self,education_level,school,department,start_year,actualResult = "• Eğitim bilgisi eklendi."):
        
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)

        beginButton = self.webdriver_wait(10,c.BEGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", beginButton) 
        sleep(3)
        beginButton.click()
        sleep(2)

        myEducationLink = self.webdriver_wait(10,c.MY_EDUCATION_LINK)
        myEducationLink.click()

        selectEducationDropdown = self.webdriver_wait(10,c.SELECT_EDUCATION_DROPDOWN)
        selectEducation = Select(selectEducationDropdown)
      
        selectEducation.select_by_visible_text(education_level)
       
        enterUniversity =self.webdriver_wait(10,c.ENTER_UNIVERSITY)
        enterUniversity.send_keys(school)
        
        deparmentName = self.webdriver_wait(10,c.DEPARTMENT_NAME)
        deparmentName.send_keys(department)

        beginDate =self.webdriver_wait(30,c.BEGIN_DATE)
        beginDate.send_keys(start_year)

        continueButton = self.webdriver_wait(20,c.CONTINUE_CSS)
        continueButton.click()

        saveButton = self.webdriver_wait(20,c.SAVE_BUTTON_CSS)
        saveButton.click()

        expectedResult = self.webdriver_wait(10,c.EXPECTED_RESULT_CSS)
        assert expectedResult.text == actualResult  
        sleep(3) 

    def test_empty_field_register(self,actualResult = "Doldurulması zorunlu alan*"):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)

        beginButton = self.webdriver_wait(10,c.BEGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", beginButton) 
        sleep(3)
        beginButton.click()
        sleep(3)

        myEducationLink = self.webdriver_wait(10,c.MY_EDUCATION_LINK)
        myEducationLink.click()

        saveButton = self.webdriver_wait(20,c.SAVE_BUTTON_CSS)
        saveButton.click()

        expectedResult = WebDriverWait(self.driver,20).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR,c.EXPECTED_RESULT_EMPTY)))
        sleep(3)
        for i in range (len(expectedResult)):
            result = expectedResult[i]
            assert result.text == actualResult
        sleep(3)    
    