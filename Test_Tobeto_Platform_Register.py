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

#Test senaryosu 2:  Kullanıcının siteye kayıt olabilmesi durumu doğrulanacaktır.
        
class Test_Tobeto_Platform_Register:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.REGISTER_URL)
        self.driver.maximize_window()

    def teardown_method(self): 
        self.driver.quit()
    
    def test_successful_register(self):
        firstnameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_FIRST_NAME_XPATH)))
        firstnameInput.send_keys("testad")
        lastnameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_LAST_NAME_XPATH)))
        lastnameInput.send_keys("testsoyad")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_MAIL_XPATH)))
        emailInput.send_keys("testtest@gmail.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_PASSWORD_XPATH)))
        passwordInput.send_keys("test456")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_PASSWORD_AGAIN_XPATH)))
        passwordAgainInput.send_keys("test456")
        registerButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_SEND_BUTTON_XPATH)))
        registerButton.click()
        checkboxcontact = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_CONTACT_XPATH)))
        checkboxcontact.click()
        checkboxmembershipContrat = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_MEMBERSHIP_CONTRAT_XPATH)))
        checkboxmembershipContrat.click()
        checkboxemailConfirmation = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_EMAIL_CONFIRMATION_XPATH)))
        checkboxemailConfirmation.click()
        checkboxphoneConfirmation = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_PHONE_CONFIRMATION_XPATH)))
        checkboxphoneConfirmation.click()
        checkboxphoneInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_PHONE_INPUT_XPATH)))
        checkboxphoneInput.send_keys("5355353535")
        iframe = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        reCAPTCHA = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.RECAPTCHA_CHECBOX_XPATH)))
        reCAPTCHA.click()
        sleep(10)
        self.driver.switch_to.default_content()
        continueButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.CONTINUE_BUTTON_XPATH)))
        continueButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH, c.REGISTER_SYSTEM_SUCCESSFUL_MESSAGE_XPATH)))
        assert systemMessage.text == "Tobeto Platform'a kaydınız başarıyla gerçekleşti."
        sleep(10)

    @pytest.mark.parametrize("Email", [("abc.+4"),("e"),("günes")])
    def test_invalid_email_register(self,Email):
        firstnameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_FIRST_NAME_XPATH)))
        firstnameInput.send_keys("testad")
        lastnameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_LAST_NAME_XPATH)))
        lastnameInput.send_keys("testsoyad")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_MAIL_XPATH)))
        emailInput.send_keys(Email)
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_MAIL_ERROR_MESSAGE_XPATH)))
        assert errorMessage.text == "Geçersiz e-posta adresi*"

    def test_invalid_phone_number_1(self):
        firstnameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_FIRST_NAME_XPATH)))
        firstnameInput.send_keys("testad")
        lastnameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_LAST_NAME_XPATH)))
        lastnameInput.send_keys("testsoyad")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_MAIL_XPATH)))
        emailInput.send_keys("test456@hotmail.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_PASSWORD_XPATH)))
        passwordInput.send_keys("test456")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_PASSWORD_AGAIN_XPATH)))
        passwordAgainInput.send_keys("test456")
        registerButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_SEND_BUTTON_XPATH)))
        registerButton.click()
        checkboxcontact = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_CONTACT_XPATH)))
        checkboxcontact.click()
        checkboxmembershipContrat = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_MEMBERSHIP_CONTRAT_XPATH)))
        checkboxmembershipContrat.click()
        checkboxemailConfirmation = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_EMAIL_CONFIRMATION_XPATH)))
        checkboxemailConfirmation.click()
        checkboxphoneConfirmation = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_PHONE_CONFIRMATION_XPATH)))
        checkboxphoneConfirmation.click()
        checkboxphoneInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_CHECK_BOX_PHONE_INPUT_XPATH)))
        checkboxphoneInput.send_keys("53553535")
        iframe = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        reCAPTCHA = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.RECAPTCHA_CHECBOX_XPATH)))
        reCAPTCHA.click()
        self.driver.switch_to.default_content()
        continueButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.CONTINUE_BUTTON_XPATH)))
        continueButton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.PHONE_NUMBER_ERROR_MESSAGE1_XPATH)))
        assert errorMessage.text == "En az 10 karakter girmelisiniz."
        sleep(5)