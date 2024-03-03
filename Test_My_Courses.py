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
from Valid_Login import Test_Valid_Login

class Test_My_Courses:

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()     

    def test_my_courses(self):

        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("busraaaydinn67@gmail.com","********")
        sleep(3)

        self.driver.execute_script("window.scrollTo(0,700)")

        myCoursesButton = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.ID, c.MY_COURSES)))
        sleep(3)
        myCoursesButton.click()
        sleep(3)

        showMoreButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.SHOW_MORE_BUTTON)))
        showMoreButton.click()
        sleep(3)

        searchButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.SEARCH_BUTTON)))
        searchButton.send_keys("h")
        sleep(5)

        courseController = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.COURSE_CONTROLLER)))
        assert courseController.text == "Eğitime Git" 
        
        searchButton.clear()
        sleep(5)
        
        searchButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.SEARCH_BUTTON)))
        searchButton.send_keys("w")
        sleep(5)

        courseNotFoundController = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.COURSE_NOT_FOUND_CONTROLLER)))
        assert courseNotFoundController.text == "Size atanan herhangi bir eğitim bulunmamaktadır." 

        self.driver.get("https://tobeto.com/egitimlerim")
        self.driver.refresh()
        sleep(5)
         
        selectInstitution = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.SELECT_INSTITUTION)))
        selectInstitution.click()

        istanbulCoding = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.ISTANBUL_CODING_ID)))
        istanbulCoding.click()            
        sleep(3)

        filterController = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.FILTER_CONTROLLER)))
        assert filterController.text == "İstanbul Kodluyor" 

        removeFilters = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.REMOVE_FILTERS)))
        removeFilters.click()            
        sleep(3)

        removeFilterController = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.REMOVE_FILTER_CONTROLLER)))
        assert removeFilterController.text == "Kurum Seçiniz"

        inProgress = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.IN_PROGRESS)))
        inProgress.click() 
        sleep(3) 
      
        allMyCourses = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.ALL_MY_COURSES)))
        allMyCourses.click() 
        sleep(3)
  
        completed = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.COMPLETED)))
        completed.click() 
        sleep(3)

        self.driver.execute_script("window.scrollTo(0,300)")
         
        goCourse = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.GO_COURSE)))
        sleep(5)
        goCourse.click()
        sleep(15)

        courseContentController = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.COURSE_CONTENT_CONTROLLER)))
        courseContentController.click()
        sleep(5)

