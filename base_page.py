from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Initializes a new instance of the BasePage class.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver

    def open(self, base_url):
        """
        Opens the specified URL in the browser.

        Args:
            base_url: The URL to open.
        """
        self.driver.get(base_url)

    def click(self, locator):
        """
        Performs a click action on the web element identified by the locator.

        Args:
            locator: Locator of the web element to click.
        """
        locator.click()

    def clear(self, locator):

        locator.clear()

    def network_state_idol(self):
        wait = self.wait()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.network-busy')))

    def enter_text(self, locator, text):
        """
        Enters the specified text into the web element identified by the locator.

        Args:
            locator: Locator of the web element to enter text into.
            text: The text to be entered.
        """
        locator.send_keys(text)

    def get_title(self):
        """
        Returns the title of the current page.

        Returns:
            The title of the current page.
        """
        return self.driver.title

    def switch_iframe(self, locator):
        self.driver.switch_to.frame(locator)

    def wait_for_element_to_be_visible(self, locator):
        """
        Waits until the web element identified by the locator becomes visible.

        Args:
            locator: Locator of the web element to wait for.
            timeout: Maximum time to wait in seconds (default: 10).

        Returns:
            The visible web element.
        """
        wait = self.wait()
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_present(self, locator):
        """
        Waits until the web element identified by the locator becomes present in the DOM.

        Args:
            locator: Locator of the web element to wait for.
            timeout: Maximum time to wait in seconds (default: 10).

        Returns:
            The present web element.
        """
        wait = self.wait()
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_to_be_present(self, locator):
        """
        Waits until at least one web element identified by the locator becomes present in the DOM.

        Args:
            locator: Locator of the web elements to wait for.
            timeout: Maximum time to wait in seconds (default: 10).

        Returns:
            List of present web elements.
        """
        wait = self.wait()
        return wait.until(EC.presence_of_all_elements_located(locator))

    def wait(self, timeout=10):
        w = WebDriverWait(self.driver, timeout, 3)
        return w

    def wait_for_elements_to_be_visible(self, locator):
        """
        Waits until all web elements identified by the locator become visible.

        Args:
            locator: Locator of the web elements to wait for.
            timeout: Maximum time to wait in seconds (default: 10).

        Returns:
            List of visible web elements.
        """
        wait = self.wait()
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_elements_to_be_clickable(self, locator):
        """
        Waits until all web elements identified by the locator become visible.

        Args:
            locator: Locator of the web elements to wait for.
            timeout: Maximum time to wait in seconds (default: 10).

        Returns:
            List of visible web elements.
        """
        wait = self.wait()
        return wait.until(EC.element_to_be_clickable(locator))

    def scroll_element_into_view(self, element):
        """
        Scrolls the web page to bring the specified element into view.

        Args:
            element: The web element to scroll to.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
