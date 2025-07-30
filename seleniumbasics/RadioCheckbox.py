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

login_url = "https://demo.automationtesting.in/Register.html"
driver.get(login_url)

# වෙබ් පිටුව සම්පූර්ණයෙන්ම load වීමට සුළු මොහොතක් රැඳී සිටින්න.
time.sleep(3)

# Radio Button - 'FeMale' තෝරන්න
# HTML කේතය අනුව, input tag එකට value='FeMale' ඇත.
# By.XPATH භාවිතයෙන් නිවැරදි කිරීම:
driver.find_element(By.XPATH, "//input[@value='FeMale']").click() # අනවශ්‍ය වරහන් ඉවත් කර slash ගණන නිවැරදි කර ඇත.
driver.find_element(By.XPATH, "//input[@value='Male']").click()
print("select FeMale radio button .")

# මෙතැන් සිට ඔබට අවශ්‍ය නම් අනෙකුත් ක්ෂේත්‍ර පිරවිය හැක:
# Full Name - First Name
# first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
# first_name_field.send_keys("Kamala")

# Full Name - Last Name
# last_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
# last_name_field.send_keys("Perera")

# Address
# address_field = driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']")
# address_field.send_keys("123 Main Street, Colombo")

# Email address
# email_field = driver.find_element(By.XPATH, "//input[@type='email']")
# email_field.send_keys("kamala.p@example.com")

# Phone
# phone_field = driver.find_element(By.XPATH, "//input[@type='tel']")
# phone_field.send_keys("0771234567")

# Hobbies - Cricket තෝරන්න (Check Box)
# cricket_checkbox = driver.find_element(By.ID, "checkbox1") # ID එක 'checkbox1' නම්
# cricket_checkbox.click()
# print("Cricket hobby එක තෝරාගන්නා ලදී.")


# (විකල්ප) සියලු ක්‍රියාවන් අවසන් වූ පසු බ්‍රව්සර් window එක වසන්න.
# time.sleep(5)
# driver.quit()


#check Box and get Attribute
li = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Cricket' :
        ele.click()


