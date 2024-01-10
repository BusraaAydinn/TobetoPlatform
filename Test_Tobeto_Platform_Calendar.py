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

class Test_Tobeto_Platform_Calendar:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()

    def test_calendar_open(self):
        calendarOpen = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME, "calendar-btn")))
        calendarOpen.click()
        sleep(3)

    def test_calendar_close(self):
        calendarOpen = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME, "calendar-btn")))
        calendarOpen.click()
        sleep(3)
        calendarClose = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn-close btn-close-white']")))
        calendarClose.click()
        sleep(3)