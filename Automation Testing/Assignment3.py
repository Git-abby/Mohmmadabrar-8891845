import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a new instance of Chrome WebDriver
# Provide the path to ChromeDriver

driver = webdriver.Chrome()

#MAximize the WIndow
driver.maximize_window()

options = webdriver.ChromeOptions()
options.add_argument("--port=4444")  # Change to a different port
# driver = webdriver.Chrome(options=options, executable_path="path/to/chromedriver.exe")

# Open the JOB BANK website
driver.get("https://www.jobbank.gc.ca/home")

# Wait for the page to load
wait = WebDriverWait(driver, 20)
wait.until(EC.title_contains("Job Bank"))

time.sleep(10)
# 1) Closing POP if Any
# 2) Click IT Job Link
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "j_id_5k:outOfCanadaCloseBtn"))
    )
    close_button.click()

    # Click on the career tab
    career_tab = driver.find_element("id", "quickSearch3")
    career_tab.click()
    time.sleep(10)
except:
    # If the element is not present, do something else
    career_tab = driver.find_element(By.ID, "quickSearch3")
    career_tab.click()
    time.sleep(10)

#3) Scroll Down
driver.execute_script("window.scrollBy(0, 150);")


#4) Click on The Checkbox of "Alberta"
# Locate the checkbox using the associated label text
alberta_checkbox = driver.find_element("xpath", "/html/body/main/form[2]/section/div[3]/div/section[1]/div/div[1]/label")
# Check if the checkbox is not already selected before clicking
if not alberta_checkbox.is_selected():
    alberta_checkbox.click()
time.sleep(5)

#5) Click On first Jon Posting
#Open the first job posting
Random_Job = driver.find_element("xpath", "/html/body/main/form[2]/section/div[2]/div[1]/div[3]/article[1]")
Random_Job.click()
time.sleep(3)

#6) Again Scroll Down
#to scroll 150 pixels
driver.execute_script("window.scrollBy(0, 150);")
time.sleep(3)

#7) Take Screenshot and Save it
# it will store at the path where your ".py" is saved
#Take SS and save
driver.save_screenshot("Assignment3_Screenshot.png")

# 8) Close the Driver
driver.quit()



