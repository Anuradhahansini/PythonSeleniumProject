from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.maximize_window()

login_url = "https://www.google.com/"
driver.get(login_url)

##driver.find_element(By.LINK_TEXT,'About').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'How Search works').click()