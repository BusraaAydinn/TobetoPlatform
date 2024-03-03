from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import openpyxl
from time import sleep
from constants import globalConstants as c

class Test_Chatbot:

    def setup_method(self):

        chrome_driver_path = Service("/Users/gunesgulay/Desktop/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def test_chatbot_icon_open(self):
        
        wait = WebDriverWait(self.driver, 10) 
      
        iframe = wait.until(ec.presence_of_element_located((By.ID, c.IFRAME_ID)))
        self.driver.switch_to.frame(iframe)

        launcher_button = wait.until(ec.element_to_be_clickable((By.ID, c.LAUNCHER_BUTTON)))
        sleep (5)
        launcher_button.click()
        sleep(10)

        self.driver.switch_to.default_content()

        iframe = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.IFRAME_OPEN)))
        WebDriverWait(self.driver,5).until(ec.frame_to_be_available_and_switch_to_it(iframe))

        tobetoMessage = WebDriverWait(self.driver,30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.TOBETO_MESSAGE)))
        sleep (5)
        assert tobetoMessage.text == "Merhaba 👋"
        
    def test_chatbot_icon_close(self):

        wait = WebDriverWait(self.driver, 10) 

        self.test_chatbot_icon_open()
        sleep (5)
        self.driver.switch_to.default_content()
        
        iframe_message_box = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.IFRAME_MESSAGE_BOX)))
        WebDriverWait(self.driver,5).until(ec.frame_to_be_available_and_switch_to_it(iframe_message_box))

        minimize_icon = self.driver.find_element(By.CSS_SELECTOR, c.MINIMIZE_ICON)
        minimize_icon.click()
        sleep(3)

        self.driver.switch_to.default_content()

        iframe = wait.until(ec.presence_of_element_located((By.ID, c.IFRAME_ID)))
        self.driver.switch_to.frame(iframe)
        
        chatbot_button = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.CHATBOT_BUTTON)))
    
        check_icon_close = chatbot_button.is_displayed()
        assert check_icon_close == True

    def test_end_chat(self):

        self.test_chatbot_icon_open()
        sleep (5)
        self.driver.switch_to.default_content()

        iframe = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.ID, c.IFRAME_END_CHAT)))
        self.driver.switch_to.frame(iframe)

        end_chat_button = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((By.XPATH, c.END_CHAT_BUTTON)))
        end_chat_button.click()
        sleep(5)    

        end_chat_box = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.END_CHAT_BOX)))
        check_end_chat_box = end_chat_box.is_displayed()
        assert check_end_chat_box == True
