from telnetlib import EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class UtilClass(BaseClass):

    def perform_login(driver):
        driver.find_element(By.ID, "email").send_keys("admin@kaymera.com")
        driver.find_element(By.ID, "password").send_keys("password")
        sendAccessCode = driver.find_element(By.ID, "submit")
        sendAccessCode.click()
        driver.find_element(By.ID, "accessCode").send_keys("")
        sendAccessCode = driver.find_element(By.ID, "submit")
        sendAccessCode.click()

    def trigger_reactivate_CA(self, imei):
        self.perform_login()
        self.driver.execute_script("window.devMode=true;")
        ## go to device
        ## click on rectivate CA
        self.driver.execute_script("window.devMode=false;")

    # def devices_page(driver):
    #     action = ActionChains(driver)
    #
    #     devices_button = driver.find_element(By.LINK_TEXT, "Devices")
    #     action.move_to_element(devices_button).click().perform()
    #     locator="//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button".encode('utf-8')
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, locator))
    #
    #     )
    #     print(element.text)  # 'value not used ' solution
