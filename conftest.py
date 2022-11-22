import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def setup(request):
    with open('conf/conf.json') as json_file:
        conf = json.load(json_file)

    # -------------------Your connection is not private---------------------------
    options = Options()
    options.set_capability("acceptInsecureCerts", True)
   #----NOT USEFULL
    # s = Service("/home/svetlana.kalchenko/PycharmProjects/BEautomat/chromedriver")
    # driver = webdriver.Chrome(service=s,chrome_options=options )
    #--------------
    
    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver = webdriver.Chrome(executable_path="/home/svetlana.kalchenko/PycharmProjects/BEautomat/chromedriver",chrome_options=options)
    # --------------------------------------------------------------------------

    # -------------------Your connection is not private---------------------------
    # options = Options()
    # options.set_capability("acceptInsecureCerts", True)
    # options.set_capability("ssl.client_certs.h2_coalescing_hosts", 'test.kaymera.com')
    # options.set_capability("prompt_on_multiple_matching_certificates", True)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    # --------------------------------------------------------------------------

    setup.domain = conf['baseUrl']
    url = f'{setup.domain}/assets/welcome.html'
    driver.get(url)

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()






