from util import *


# TODO UPDATE TESTS
class TestHomePageFort(BaseClass):

    def test_addFort(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        action = ActionChains(driver)
        try:
            AddDevice = driver.find_element(By.XPATH,
                                            "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")
            action.move_to_element(AddDevice).click().perform()

            addFort = driver.find_element(By.LINK_TEXT, "Add CipherFort")
            addFort.click()

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']")))
            element.send_keys("Fort")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Last Name']"))
            )
            element.send_keys("CreatedBy_Postman")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='IMEI']"))
            )
            element.send_keys("356112100551640")

            driver.find_element(By.ID, "group").click()
            groupName = driver.find_element(By.XPATH, "//*[@id='group']/option[18]")
            groupName.click()

            driver.find_element(By.ID, "policy").click()
            policy = driver.find_element(By.XPATH, "//*[@id='policy']/option[3]")
            policy.click()

            driver.find_element(By.ID, "config").click()
            config = driver.find_element(By.XPATH, "//*[@id='config']/option[27]")
            config.click()

            driver.find_element(By.ID, "expirationDateSelection").click()
            expDate = driver.find_element(By.XPATH, "//*[@id='expirationDateSelection']/option[2]")
            expDate.click()

            ok = driver.find_element(By.XPATH, "//div[@class='modal-footer ng-scope']/button[1]")
            ok.click()

        except Exception as e:

            timestr = time.strftime("%d_%m_%y-%H:%M:%S")

            logger = logging.getLogger(__name__)

            fileHandler = logging.FileHandler('logs/logfile_{0}.log'.format(timestr))

            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)

            logger.critical(e)

            # logger.critical(e, exc_info=True)

    def test_findByIMEI(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        searchField.send_keys("356112100551640")

        imei = driver.find_element(By.XPATH,
                                   "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[6]")

        try:

            assert imei.text == ' 356112100551640'

        except Exception as e:

            timestr = time.strftime("%d_%m_%y-%H:%M:%S")

            logger = logging.getLogger(__name__)

            fileHandler = logging.FileHandler('logs/logfile_{0}.log'.format(timestr))

            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)

            # logger.critical(e)

            logger.critical(e, exc_info=True)

    def test_Broadcast(self):
        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util

        searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        searchField.send_keys("356112100551640")

        checkbox = driver.find_element(By.XPATH,
                                       "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")

        actions = ActionChains(driver)
        actions.move_to_element(checkbox).perform()
        driver.execute_script("arguments[0].click();", checkbox)

        bulk_Change = driver.find_element(By.XPATH,
                                          "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
        bulk_Change.click()

        reset_Sim = driver.find_element(By.XPATH, "// ul[@class='list-unstyled'][1]/li[4]")
        reset_Sim.click()

        inputText = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/b/textarea")
        inputText.send_keys("test")

        send = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button[1]")
        send.click()

    def test_Bulk_aplllyOTA(self):

        driver = self.driver

        UtilClass.perform_login(driver)  # call a function from util

        UtilClass.devices_page(driver)  # call a function from util
        try:
            # search for device
            searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='edit-search']/div/form/input")))

            searchField.send_keys("356112100551640")
            # -----------------

            checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                       "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")))

            actions = ActionChains(driver)
            actions.move_to_element(checkbox).perform()
            driver.execute_script("arguments[0].click();", checkbox)

            bulk_Change = driver.find_element(By.XPATH,
                                              "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
            bulk_Change.click()

            apply_OTA = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[4]/ul/li[1]")))
            apply_OTA.click()
        # unavailable for "not activated" device
        # selectOTA = driver.find_element(By.ID, "//*[@id='configuration']")
        # selectOTA.click()
        #
        # OTA = driver.find_element(By.XPATH, "//*[@id='configuration']/option")
        # OTA.click()

        except Exception as e:

            timestr = time.strftime("%d_%m_%y-%H:%M:%S")

            logger = logging.getLogger(__name__)

            fileHandler = logging.FileHandler('logs/logfile_{0}.log'.format(timestr))
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)

            # logger.critical(e)
            logger.critical(e, exc_info=True)
# -------------------------------------------------------------------
