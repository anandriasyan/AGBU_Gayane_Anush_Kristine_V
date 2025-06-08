from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Helper():

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def go_to_page(self, url):
        self.driver.get(url)
        self.test_logger.info(f"{url} is opened.")

    def find_elem_ui(self, loc, sec=60):
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_element_located(loc))
            return elem
        except Exception as e:
            self.test_logger.error("Element is not vissible.")
            self.test_logger.error(e)

    def find_elm(self, loc, timout=15, get_attribute="", get_text=""):
        element = WebDriverWait(self.driver, timout).until(
            EC.presence_of_element_located(loc))
        if get_attribute:
            return element.get_attribute(get_attribute)
        elif get_text:
            return element.text
        else:
            return element

    def find_and_click(self, loc, sec=60):
        elem = WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc))
        elem.click()

    def find_and_send_keys(self, loc, inp_text, sec=60):
        elem = self.find_elem_ui(loc, sec)
        elem.send_keys(inp_text)

    def hover_and_click(self, locator):
        element = self.find_elm(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

