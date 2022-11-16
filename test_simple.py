from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def test_simple(self):
    driver = webdriver.Chrome(executable_path="/home/svetlana.kalchenko/PycharmProjects/BEautomat/chromedriver")
    driver.get("https://www.google.com/")