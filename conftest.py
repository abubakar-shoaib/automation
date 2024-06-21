import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    #options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"  # Path to Brave Browser

    # Use webdriver-manager to get the appropriate ChromeDriver
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.udemy.com/")
    request.cls.driver = driver
    time.sleep(5)
    yield
    driver.close()
