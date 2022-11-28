import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def setup(request):
    with open('conf/conf.json') as json_file:
        conf = json.load(json_file)

    # -------------------Your connection is not private---------------------------
    options = Options()
    options.set_capability("acceptInsecureCerts", True)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver = webdriver.Chrome(executable_path="/var/lib/jenkins/workspace/BEautomation-webhook/chromedriver",chrome_options=options)
    # --------------------------------------------------------------------------


    setup.domain = conf['baseUrl']
    url = f'{setup.domain}/assets/welcome.html'
    driver.get(url)

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()






