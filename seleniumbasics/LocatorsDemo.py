from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome Options සකස් කිරීම
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# 1. Chrome Driver එක ආරම්භ කරන්න
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)

 #2. Browser Window එක පුළුල් කරන්න (Maximize කරන්න)
driver.maximize_window() # මෙය තමයි browser එක පුළුල් කරන කේතය!
print("Browser window එක පුළුල් කරන ලදී.")


# 3. Login පිටුවට යන්න
login_url = "http://102.130.127.112:7001/Login"
driver.get(login_url)

# 3. වෙබ් පිටුව සම්පූර්ණයෙන්ම load වීමට සුළු මොහොතක් රැඳී සිටින්න.
time.sleep(3)

# 4. Username ක්ෂේත්‍රය සොයාගෙන "admin" ඇතුළත් කරන්න
# රූපය අනුව Username ක්ෂේත්‍රයේ ID එක 'username' (කුඩා අකුරු) බවට උපකල්පනය කර ඇත.
# ඔබගේ පෙර රූපයේ 'Username' ලෙස Capital U එකකින් තිබුණත්,
# සාමාන්‍යයෙන් ID's lowercase භාවිතා වේ.
# අවශ්‍ය නම්, මෙය "Username" ලෙස නැවත වෙනස් කළ හැක.
username_text = driver.find_element(By.ID, 'username')
username_text.send_keys("admin")
print("Username: 'admin' ඇතුළත් කරන ලදී.")

# 5. Password ක්ෂේත්‍රය සොයාගෙන "admin123" ඇතුළත් කරන්න
# රූපය අනුව Password ක්ෂේත්‍රයේ ID එක 'password' (කුඩා අකුරු) බව පැහැදිලියි.
password_text = driver.find_element(By.ID, "password") # මෙතන 'password' ලෙස කුඩා අකුරින්!
password_text.send_keys("admin123")
print("Password: 'admin123' ඇතුළත් කරන ලදී.")

# 6. Login බොත්තම සොයා ගන්න
# රූපයේ දැක්වෙන පරිදි, බොත්තමට class="login-button" සහ text content "Sign In" ඇත.
login_button = driver.find_element(By.XPATH, "//button[text()='Sign In']")
print("Login බොත්තම සාර්ථකව සොයා ගන්නා ලදී.")

# 7. Login බොත්තම ක්ලික් කරන්න
login_button.click()
print("Login බොත්තම ක්ලික් කරන ලදී.")

# 8. (විකල්ප) Login වීමෙන් පසු පිටුව load වන තෙක් රැඳී සිටින්න.
time.sleep(5)

# 9. (විකල්ප) Login වීමෙන් පසු පිටුවේ මාතෘකාව (title) පරීක්ෂා කිරීම.
print(f"Login වීමෙන් පසු පිටුවේ මාතෘකාව: {driver.title}")

# 10. (විකල්ප) වැඩේ අවසන් වූ පසු බ්‍රව්සර් window එක වසන්න.
# driver.quit()
# print("Browser window එක වසා දමන ලදී.")