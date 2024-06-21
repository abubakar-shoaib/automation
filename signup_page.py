import time
from selenium.webdriver.common.by import By
from base_page import BasePage


class Signup(BasePage):
    #getting locators and save into the variable

    SignupLocator = '.ud-btn.ud-btn-medium.ud-btn-primary.ud-heading-sm'
    username_input_field = 'fullname'
    email_input_field = 'email'
    password_input_field = 'password'
    sign_in_button = 'submit'


    def __init__(self, browser):
        """
            Initialize the DemoPage class.

            Args:
                browser: WebDriver instance.

            Returns:
                None.
            """
        super().__init__(browser)
    #inputting  the username
    def SignupClick(self):
        self.wait_for_element_to_be_visible((By.CSS_SELECTOR, self.SignupLocator)).click()
        time.sleep(5)

    def username(self, text):
        self.enter_text(self.wait_for_element_to_be_visible((By.NAME, self.username_input_field)), text)
        time.sleep(5)

    def email(self, text):
        self.enter_text(self.wait_for_element_to_be_visible((By.NAME, self.email_input_field)), text)
        time.sleep(5)

    def password(self, text):
        self.enter_text(self.wait_for_element_to_be_visible((By.NAME, self.password_input_field)), text)
        time.sleep(5)

    def click_sign_in_button(self):
        self.click(self.wait_for_elements_to_be_clickable((By.NAME, self.sign_in_button)))
        time.sleep(5)
