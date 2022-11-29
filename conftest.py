import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def setup(request):
    with open('conf/conf.json') as json_file:
        conf = json.load(json_file)

    # ------------------------------------------------------------------------
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--crash-dumps-dir=/tmp')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    # --------------------------------------------------------------------------

    setup.domain = conf['baseUrl']
    url = f'{setup.domain}/assets/welcome.html'
    driver.get(url)

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()
