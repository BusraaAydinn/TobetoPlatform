import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Valid_Login import Test_Valid_Login

class Test_Platform:
    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()    

    def test_button_controls(self):
            
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("busraaaydinn67@gmail.com","*******")
        sleep(3)  

        self.driver.execute_script("window.scrollTo(0,600)")

        myCourses = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.MY_COURSES)))
        sleep(5)
        myCourses.click()
        sleep(2)

        coursesController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.COURSES_CONTROLLER)))
        sleep (2)
        assert coursesController.text == "Eğitime Git"
        sleep(2)
    
        myAnnouncementsNews = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.NOTIFICATION)))
        myAnnouncementsNews.click()
        sleep(2)

        newsController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.NEWS_CONTROLLER)))
        assert newsController.text == "Duyuru"
        sleep(2)

        mySurveys = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.SURVEY)))
        mySurveys.click()
        sleep(3)

        surveyController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.SURVEY_CONTROLLER)))
        assert surveyController.text == "Atanmış herhangi bir anketiniz bulunmamaktadır"
        sleep(2)
            
        myApplications = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.APPLY)))
        myApplications.click()
        sleep(2)   