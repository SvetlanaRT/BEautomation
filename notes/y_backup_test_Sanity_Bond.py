import conftest
from util import *
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_loginPage(self):
        driver = self.driver

        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "km-welcome")))
        element = element

        current_url = driver.current_url
        try:
            assert current_url == f'{conftest.setup.domain}/assets/welcome.html'
        except:
            "Error!login_Page"
            UtilClass.logging(driver)  # call a function from util

    def test_login(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Dashboard")))
        element = element  # 'value not used ' solution

        current_url = driver.current_url
        try:
            assert current_url == f'{conftest.setup.domain}/assets/index.html#/dashboard/system'

        except:
            "Error! test_Login"
            UtilClass.logging(driver)  # call a function from util

    # error
    def test_Devices(self):
        driver = self.driver
        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "km-outlet-toolbar")))
        element = element

        Current_URL = driver.current_url
        try:
            assert Current_URL == f'{conftest.setup.domain}/assets/index.html#/devices/list/org/57d686cce4b046fcd03efcc6/detailed'

        except TimeoutException:
            "Error! test_Devices!"
            UtilClass.logging(driver)  # call a function from util

    def test_addDeviceDropDownMenu(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        action = ActionChains(driver)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")))
        element = element  # 'value not used ' solution
        try:
            AddDevice = driver.find_element(By.XPATH,
                                            "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")
            action.move_to_element(AddDevice).click().perform()

            expected_list = ["Add CipherFort 2.0", "Add CipherFort", "Add CipherBond", "Add CipherWatch", "Upload CSV"]
            curent_list = [element.text for element in
                           driver.find_elements(By.XPATH, '//ul[@class="dropdown-menu right"]/li')]

            assert expected_list == curent_list

        except TimeoutException:
            "Error! DropDownMenu not as Expected!"
            UtilClass.logging(driver)  # call a function from util

    def test_addBond(self):
        driver = self.driver
        try:
            UtilClass.perform_login(driver)  # call a function from util

            UtilClass.devices_page(driver)  # call a function from util

            add_device_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button")))
            add_device_button.click()

            addBond = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add CipherBond")))
            addBond.click()

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='First Name']"))
            )
            element.send_keys("Bond")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Last Name']"))
            )
            element.send_keys("CreatedBy_Postman")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Email']"))
            )
            element.send_keys("svetlana.kalchenko@kaymera.com")

            driver.find_element(By.ID, "group").click()
            groupName = driver.find_element(By.XPATH, "//*[@id='group']/option[18]")
            groupName.click()

            driver.find_element(By.ID, "config").click()
            config = driver.find_element(By.XPATH, "//*[@id='config']/option[27]")
            config.click()

            driver.find_element(By.ID, "expirationDateSelection").click()
            exp_date = driver.find_element(By.XPATH, "//*[@id='expirationDateSelection']/option[2]")
            exp_date.click()

            ok = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='modal-footer ng-scope']/button[1]")))
            ok.click()
        except:
            "Error!Test_addBond!"
            UtilClass.logging(driver)

    def test_find_by_email(self):
        driver = self.driver
        try:
            UtilClass.perform_login(driver)  # call a function from util

            UtilClass.devices_page(driver)  # call a function from util

            search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='edit-search']/div/form/input")))

            search_field.send_keys("svetlana.kalchenko@kaymera.com")

        except:
            "Error! Test_find_by_email!"
            UtilClass.logging(driver)  # call a function from util

    # TODO! no option to delete

    # def test_DeleteByEmail(self):
    #     driver = self.driver
    #
    #     checkBox=driver.find_element(By.XPATH,"//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")
    #     checkBox.click()

    # bulk_Change=driver.find_element(By.XPATH,"//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
    # bulk_Change.click()

    # TODO!

    def test_resetSIM(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util
        # search for device
        search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        search_field.send_keys("svetlana.kalchenko@kaymera.com")
        # -----------------

        checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")))

        actions = ActionChains(driver)
        actions.move_to_element(checkbox).perform()
        driver.execute_script("arguments[0].click();", checkbox)

        bulk_Change = driver.find_element(By.XPATH,
                                          "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
        bulk_Change.click()

        reset_Sim = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[1]/ul/li[4]")))
        reset_Sim.click()

        alertOK = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")
        alertOK.click()

    # TODO  asertion
    def test_editBond(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        # search for device
        search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        search_field.send_keys("svetlana.kalchenko@kaymera.com")
        # -----------------

        checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")))

        actions = ActionChains(driver)
        actions.move_to_element(checkbox).perform()
        driver.execute_script("arguments[0].click();", checkbox)

        deviceBond = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]")))
        deviceBond.click()

        editButton = driver.find_element(By.XPATH, "//*[@id='device-details']/div/div[1]/span[2]/div/button[2]")
        editButton.click()

        lastNameInput = driver.find_element(By.XPATH, "//input[@id='lastname']")
        lastNameInput.clear()
        lastNameInput.send_keys("updatedBy_Postman")

        saveButton = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")
        saveButton.click()

        fullName = driver.find_element(By.XPATH,
                                       "//*[@id='device-details']/div/div[2]/div/div/div[1]/div[2]/label[1]/span")
        updatedName = fullName.text

        assert updatedName == "Bond updatedBy_Postman"

    # for internal_use

    def test_logging(self):
        driver = self.driver
        UtilClass.logging(driver)
