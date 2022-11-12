# driver.execute_script('browserstack_executor: {"action": "acceptSsl"}')

# my_thread = threading.Thread(target=manage_os_popup)
# my_thread.start()
#
# driver.get(url)
# res = driver. \
#     execute_script("return document.documentElement.outerHTML")


# parent = driver.current_window_handle
# uselessWindows = driver.window_handles
# for winId in uselessWindows:
#     if winId != parent:
#         driver.switch_to.window(winId)


# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".modal-header.ng-scope"))
#
# time.sleep(2)
# print(driver.current_url)
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "form-control ng-pristine ng-invalid ng-invalid-required ng-valid-maxlength ng-touched"))
# )
# element.send_keys("Bond")

# driver.find_element(By.CSS_SELECTOR,
#                     "form-control ng-pristine ng-untouched ng-invalid ng-invalid-required ng-valid-maxlength").send_keys(
#     "Postman")


# # create action chain object
# action = ActionChains(driver)
#
# # perform the operation
# action.move_to_element(element).click().perform()

# ------------------------

# select = Select(driver.find_element(By.XPATH, "//ul[@class='dropdown-menu right']"))
#
# select.select_by_visible_text('Add CipherBond')
# ERROR: Select only works on <select> elements, not on <ul>


# -------------LOGGER-----------------------
# logging.critical(e, exc_info=True)
#
# timestr = time.strftime("%d_%m_%y-%H:%M:%S")
#
# logger = logging.getLogger(__name__)
# fileHandler = logging.FileHandler('logs/logfile_{0}.log'.format(timestr))
# formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
# fileHandler.setFormatter(formatter)
# logger.addHandler(fileHandler)
# logger.setLevel(logging.INFO)

# logger.debug("A debug statement is executed")
# logger.info("An info message is executed")
# logger.warning("A warning message is executed")
# logger.error("An error message is executed")
# logger.critical(A critical message is executed)


# pytest --html=report.html.
