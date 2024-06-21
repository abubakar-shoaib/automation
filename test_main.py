import pytest
from signup_page import Signup
import time

@pytest.mark.usefixtures("setup")
class TestMain:
    @pytest.fixture(autouse=True)
    def class_setup(self, request):
        self.signup_page = Signup(request.cls.driver)

    def test_signup_click(self):
        self.signup_page.SignupClick()
        time.sleep(50)
    def test_should_login_to_website(self):
        self.signup_page.username("ashoaib")
        self.signup_page.email("ashoaib@gmail.com")
        self.signup_page.password("Bim12345@")
        self.signup_page.click_sign_in_button()
