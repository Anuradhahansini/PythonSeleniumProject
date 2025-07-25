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

#Xpath

#Sytax
#//tagname[@attribute ='value'] or //*[@attribute ='value']
#//input[@placeholder='First Name']
#//*[@placeholder='First Name']


#text
#//label[text() ='Full Name* ']  can get full value

#Contains
#//label[contains(text(),'Full Name')]  can get partial value
#index
#//label[3]

#OR & AND
#//*[@placeholder='First Name' and @ng-model="FirstName"]
#//*[@placeholder='First Name' or ng-model="FirstName"]
#parent - Child - ancestor
#//form[@id= 'basicBootstrapForm']/child::div  direct child
#//form[@id= 'basicBootstrapForm']//child::div  multi child

#//form[@id= 'basicBootstrapForm']/parent::div  direct child
#//form[@id= 'basicBootstrapForm']/ancestor::div  direct child


#following - sibling - preceding
#//input[@id='checkbox1']//following-sibling::label
#//input[@id='checkbox1']//preceding-sibling::label