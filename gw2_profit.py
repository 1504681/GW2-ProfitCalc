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

#What professions do I have?
weaponsmith = True
huntsman = True
artificer = False
armorsmith = False
leatherworker = True
tailor = False
jeweler = True
chef = True
scribe = True
other = True


#What are my gold values?

TotalGold = 70
GoldToSpend = TotalGold * 0.8 #So we have enough money leftover to re-list items
GoldPerHour = GoldToSpend / 12
DaysWorth = 1 #Get all the materials you need to max out daily

#Minimum Profit (in Copper)
MinProfit = 150 # 1 Silver 50 copper
MinPercentProfit = 10
MinVelocity = 10 #Velocity is roughly the amount of time an item is traded per day, higher velocity = quicker trades

#Included Disciplines

def JobTicked(job, string):
	box = driver.find_element_by_name(string)
	if job:
		if not box.is_selected():
			box.click()
	if not job:
		if box.is_selected():
			box.click()

#Check all jobs and tick box if have job and box not ticked
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lessfade"))
    )
finally:
    a = 1 + 1
JobTicked(weaponsmith,"Weaponsmith")
JobTicked(artificer,"Artificer")
JobTicked(armorsmith,"Armorsmith")
JobTicked(leatherworker,"Leatherworker")
JobTicked(tailor,"Tailor")
JobTicked(jeweler,"Jeweler")
JobTicked(chef,"Chef")
JobTicked(scribe,"Scribe")
JobTicked(other,"Other")

#ChangeTextBoxFunction
def ChangeBox(elementname, var):
	box = driver.find_element_by_name(elementname)
	box.clear()
	box.send_keys(str(var))

ChangeBox("amount",DaysWorth)
ChangeBox("max_gold",GoldToSpend)
ChangeBox("min_g_hr",GoldPerHour)
ChangeBox("minimum_limit",MinProfit)
ChangeBox("percent_limit",MinPercentProfit)
ChangeBox("velocity_limit",MinVelocity)


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
materialTable = driver.find_element_by_tag_name("tbody")
matTableNumRow = len (driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/form/table[2]/tbody/tr"))
#print(matTableNumRow)
rows = materialTable.find_elements(By.XPATH, "/html/body/table/tbody/tr[2]/td/form/table[2]/tbody") # get all of the rows in the table
for row in rows:
	#Get Columns
	dataset = row.find_elements(By.TAG_NAME, "tr")
	for data in dataset:
		data = print(data.text)
		print("======================") #Seperate data with a divider


#After we get all the info we need, lets close the browser
#driver.quit()
