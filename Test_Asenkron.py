import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Valid_Login import Test_Valid_Login

class Test_Asenkron:

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def test_go_asenkron_course(self):
            
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("busraaaydinn67@gmail.com","********")
        sleep(3)

        self.driver.execute_script("window.scrollTo(0,300)")

        myCoursesButton = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.ID, c.MY_COURSES)))
        sleep(3)
        myCoursesButton.click()
        sleep(3)

        self.driver.execute_script("window.scrollTo(0,700)")

        showMoreButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.SHOW_MORE_BUTTON)))
        sleep(5)
        showMoreButton.click()
        sleep(3)

        self.driver.execute_script("window.scrollTo(0,1200)")

        goAsenkronCourse = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.GO_ASENKRON_COURSE)))
        sleep(5)
        goAsenkronCourse.click()
        sleep(10)

        asenkronCourseController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.ASENKRON_COURSE_CONTROLLER)))
        assert asenkronCourseController.text == "İçerik"
        sleep(3)
        
    def test_asenkron_like(self):

        self.test_go_asenkron_course()

        iconLike = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, c.ICON_LIKE)))
        iconLike.click()
        sleep(3)
        
    def test_asenkron_undo_like(self):

        self.test_go_asenkron_course()

        iconDislike = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.ICON_DISLIKE)))
        iconDislike.click()
        sleep(3)

        assert False 
        print ("'Favorileriden çıkarma işlemin başarıyla gerçekleşti.' uyarısı görüntülenememektedir.")
        
    def test_view_likers(self):

        self.test_go_asenkron_course()

        viewPerson = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, c.VIEW_PERSON)))
        viewPerson.click()
        sleep(3)

        likersController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.LIKERS_CONTROLLER)))
        assert "Beğenenler" in likersController.text 
        sleep(3)

        
    def test_about_content(self):

        self.test_go_asenkron_course()
        
        aboutContentButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.ABOUT_CONTENT_BUTTON)))
        aboutContentButton.click()
        sleep(5)
 
        aboutContentController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.ABOUT_CONTENT_CONTROLLER)))
        assert aboutContentController.text == "Başlangıç"
        sleep(3)
        