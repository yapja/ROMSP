from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


# Starts headless Firefox and redirect to Yggdrail Daily Login page
# service_log_path disables geckodriver logging
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options, service_log_path='NUL')
driver.get("https://activities.roextreme.com/ragnarok-msp-yggdrasil/daily-login")

# Reads file where username and password is stored
with open('credentials.json', 'r') as from_file:
    data = from_file.read()
credentials = json.loads(data)

# Logins each account and claims the reward
for account in credentials['credentials']:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/button').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[1]/input[1]').send_keys(account['username'])
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[1]/input[2]').send_keys(account['password'])
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    if (len(driver.find_elements_by_css_selector('div[class="BoxItem active"]')) > 0):
        driver.find_element_by_css_selector('div[class="BoxItem active"]').click()
        driver.find_element_by_xpath('//*[@id="send-item-btn"]').click()
        print("Daily login reward claimed for {}!".format(account['username']))
    else:
        print("Daily login reward already claimed for {}!".format(account['username']))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/a').click()

# Terminates WebDriver session
driver.quit()

input('Press any key to exit!')