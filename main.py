import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "EMAIL ACCOUNT"
ACCOUNT_PASSWORD = "ACCOUNT PASSWORD"

# chromedriver_autoinstaller.install()
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()

#### Signing up with email and password in LinkedIn #####
# driver.get("https://www.linkedin.com/")
job = ""
driver.get("https://www.linkedin.com/jobs/jobs-in-toshkent?trk=homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
sign_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(5)

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(ACCOUNT_PASSWORD)
button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
button.click()
search = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember26"]')
search.send_keys("Python")
all_filter = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/div/div')
all_filter.click()
easy_apply = driver.find_element(By.XPATH, '//*[@id="ember582"]/ul/li[7]/fieldset/div')
easy_apply.click()
search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]')
search_button.click()
first_result = driver.find_element(By.XPATH, '//*[@id="ember892"]/h2')
print(first_result.text)
choice = input(f"Do want to apply to {first_result.text}? Say yes or no: ")
if choice == "yes":
    applying = driver.find_element(By.XPATH, '//*[@id="ember913"]')
    if applying.get_attribute("role").text == "link":
        print("Sorry, you should apply with website")
    job = first_result.text
else:
    second_job = driver.find_element(By.XPATH, '//*[@id="ember802"]')
    second_job.click()
    second_job_name = driver.find_element(By.XPATH, '//*[@id="ember892"]/h2')
    print(f"Your second choice: {second_job_name.text}")
    easy_apply2 = driver.find_element(By.XPATH,
                                      '//*[@id="ember938"]')
    easy_apply2.click()
    phone_number2 = driver.find_element(By.XPATH,
                                        '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div[2]/div/div/input')
    phone_number2.send_keys("945653215")
    next_button2 = driver.find_element(By.XPATH, '//*[@id="ember954"]')
    next_button2.click()
    job = second_job_name.text

print(f"You have successfully applied to {job}")
