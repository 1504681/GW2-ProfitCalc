from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Change this path to wherever you installed your chromedriver

#Webdriver Setup
PATH = "D:\dev\GW2-ProfitCalc\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.gw2profits.com/craft_everything.php")



#Lets declare variables.
#What are my skills?
chef = True
tailor = False
#What are my gold values?

TotalGold = 70
GoldToSpend = TotalGold * 0.8
GoldPerHour = GoldToSpend / 12
DaysWorth = 0.3


#Included Disciplines

#Chef
chefBox = driver.find_element_by_name("Chef")
'''
if chef:
	if chefBox.value
	chefbox.click
'''



#Lets get the AmountToMake x Day's Worth Textbox
amountBox = driver.find_element_by_name("amount")
amountBox.clear()
amountBox.send_keys(str(DaysWorth))

#Max Gold to Spend
max_goldBox = driver.find_element_by_name("max_gold")
max_goldBox.clear()
max_goldBox.send_keys(str(GoldToSpend))

#Max Gold to Spend
min_g_hBox = driver.find_element_by_name("min_g_hr")
min_g_hBox.clear()
min_g_hBox.send_keys(str(GoldPerHour))



#The form is filled out, lets hit the Update Settings button
updateButton = driver.find_element_by_name("update_settings")
updateButton.click()

#Explicit wait for the table to show up
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lessfade"))
    )
finally:
    a = 1 + 1


#Now lets get the name of every Material to Collect

materialTable = driver.find_element_by_class_name("lessfade")
matTableNumRow = len (driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/form/table[2]/tbody/tr"))
print(matTableNumRow)

#After we get all the info we need, lets close the browser
#driver.quit()
