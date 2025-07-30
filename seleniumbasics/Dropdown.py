import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import  Select
import time

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.maximize_window()

login_url = "https://demo.automationtesting.in/Register.html"
driver.get(login_url)

#Select Class declaration with Webelement  # Dropdown (Select element)
select_web = driver.find_element(By.ID,'Skills') #'Skills' කියන ID එක තියෙන Dropdown box එක (HTML එකේ <select> tag එක) අපි හොයාගෙන, ඒක select_web කියන variable එකට දානවා.
sel = Select(select_web) #Dropdown එකක Options තෝරන්න Selenium වලට වෙනමම "Select" කියලා Class එකක් තියෙනවා.  අපි මේ පේළියෙන් කරන්නේ, කලින් හොයාගත්තු select_web කියන Dropdown box එක පාවිච්චි කරන්න Select Class එකේ sel කියලා Object එකක් හදන එක. මේ sel Object එක පාවිච්චි කරලා Dropdown එකේ Options තෝරන්න පුළුවන්.

#Select by Index
#sel.select_by_index(5) #select_by_index(): මේකෙන් කරන්නේ Dropdown එකේ Options වල අංකයට අනුව තෝරන එක   5 කියන්නේ හයවෙනි Option එක තෝරනවා කියන එක.

#select by value #මේකෙන් කරන්නේ Dropdown එකේ තියෙන Option එකක HTML value ගුණාංගයට අනුව තෝරන එක.
sel.select_by_value('Configuration')

#Select by visible text #මේකෙන් කරන්නේ Dropdown එකේ Option එකක අපිට පේන text එක (වෙබ් අඩවියේ පෙනෙන text එක) අනුව තෝරන එක.  <option value="...">Design</option> වගේ තියෙන Option එකක් මේකෙන් තෝරනවා. (එනම්, Design යන වචනය පේන Option එක තෝරනවා
sel.select_by_visible_text('Design')


print(driver.current_url)

#navigato Different URL
driver.get('https://www.google.com/')

print(driver.current_url)
#back  #මේක හරියට browser එකේ තියෙන "Back" බොත්තම click කරනවා වගේ වැඩක්.
driver.back()
#refresh #මේක browser එකේ තියෙන "Refresh" බොත්තම click කරනවා වගේ වැඩක්.
driver.refresh()
#forward #මේක browser එකේ තියෙන "Forward" බොත්තම click කරනවා වගේ වැඩක්.
driver.forward()

#close #මේක ඉතා වැදගත්! මේකෙන් කරන්නේ විවෘත කර ඇති Chrome browser window එක සම්පූර්ණයෙන්ම වසා දාන එක
driver.quit()



