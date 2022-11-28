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
    
    #driver solution------------------------------------------------------------
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--headless')
    
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    #----------------------------------------------------------------------------
    
    options.set_capability("acceptInsecureCerts", True)
    driver = webdriver.Chrome(chrome_options=options)

    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    #driver = webdriver.Chrome(executable_path="/home/svetlanakalchenko/PycharmProjects/BEautomation/chromedriver",chrome_options=options)
    
    # --------------------------------------------------------------------------


    setup.domain = conf['baseUrl']
    url = f'{setup.domain}/assets/welcome.html'
    driver.get(url)

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()






