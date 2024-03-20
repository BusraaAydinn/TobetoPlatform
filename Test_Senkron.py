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

class Test_Senkron:

    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def test_go_senkron_course(self):
            
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("gunesgulay@icloud.com","unutma34")
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

        goSenkronCourse = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.GO_SENKRON_COURSE)))
        sleep(5)
        goSenkronCourse.click()
        sleep(10)

        senkronCourseController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.SENKRON_COURSE_CONTROLLER)))
        assert senkronCourseController.text == "İçerik"
        sleep(3)    

    def test_senkron_like(self):

        self.test_go_senkron_course()

        iconLike = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, c.ICON_LIKE)))
        iconLike.click()
        sleep(3)

    def test_senkron_undo_like(self):

        self.test_go_senkron_course()

        iconDislike = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.ICON_DISLIKE)))
        iconDislike.click()
        sleep(3)      

        assert False 
        print ("'Favorileriden çıkarma işlemin başarıyla gerçekleşti.' uyarısı görüntülenememektedir.")

    def test_view_likers(self):

        self.test_go_senkron_course()

        viewPerson = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME, c.VIEW_PERSON)))
        viewPerson.click()
        sleep(3)

        likersController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.LIKERS_CONTROLLER)))
        assert "Beğenenler" in likersController.text 
        sleep(3)    

    def test_about_content(self):

        self.test_go_senkron_course()
        
        aboutContentButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.ABOUT_CONTENT_BUTTON)))
        aboutContentButton.click()
        sleep(5)
 
        aboutContentController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.ABOUT_CONTENT_CONTROLLER)))
        assert aboutContentController.text == "Başlangıç"
        sleep(3)      

    def test_view_detail(self):

        self.test_go_senkron_course()

        viewDetailButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.VIEW_DETAIL_BUTTON)))
        viewDetailButton.click()
        sleep(5)

        detailController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.DETAIL_CONTROLLER)))
        assert detailController.text == "SANAL SINIF"
        sleep(3) 

    def test_open_record(self):

        self.test_go_senkron_course()

        openRecordButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, c.OPEN_RECORD_BUTTON)))
        openRecordButton.click()
        sleep(15)

      


