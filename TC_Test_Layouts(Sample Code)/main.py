import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_URL = "https://app.usepanda.com/#/"


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_layouts(driver):
    driver.get(LOGIN_URL)
    time.sleep(5)
    driver.refresh()
    time.sleep(3)
    layouts = driver.find_element(By.XPATH,"//i[@class='flaticon stroke layout-1']")
    layouts.click()
    layout_2 = driver.find_element(By.XPATH,"(//img[@class='layout-image'])[2]")
    layout_2.click()
    time.sleep(3)


