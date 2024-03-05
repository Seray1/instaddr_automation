from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


account_id = "enter your id here"
password = "enter your password here"

driver = webdriver.Chrome()
driver.get("https://m.kuku.lu/index.php")
wait = WebDriverWait(driver, 30)
current_time = datetime.now()

login_element = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="link_loginform"]'))
)
driver.execute_script("arguments[0].scrollIntoView();", login_element)
driver.execute_script("arguments[0].click();", login_element)
time.sleep(1)


account_id_element = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="user_number"]'))
)
driver.execute_script("arguments[0].scrollIntoView();", account_id_element)
driver.execute_script("arguments[0].value = arguments[1];", account_id_element, account_id)
time.sleep(1)
password_element = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="user_password"]'))
)
driver.execute_script("arguments[0].scrollIntoView();", password_element)
driver.execute_script("arguments[0].value = arguments[1];", password_element, password)
time.sleep(1)
login_element2 = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="area_loginform"]/div/form/div[4]/a'))
)
driver.execute_script("arguments[0].scrollIntoView();", login_element2)
driver.execute_script("arguments[0].click();", login_element2)
time.sleep(2)
merge_element = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="area-confirm-dialog-button-cancel"]'))
)
driver.execute_script("arguments[0].scrollIntoView();", merge_element)
driver.execute_script("arguments[0].click();", merge_element)
time.sleep(3)
def generate_emails():
    terms_of_use = True
    for i in range(895):
        try:
            create_email_element = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="link_addMailAddrByAuto"]')
                )
            )
            driver.execute_script(
                "arguments[0].scrollIntoView();", create_email_element
            )
            driver.execute_script(
                "arguments[0].click();", create_email_element
            )
            if terms_of_use:
                yes_terms_element = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="area-confirm-dialog-button-ok"]')
                    ))
                driver.execute_script("arguments[0].scrollIntoView();", yes_terms_element)
                driver.execute_script("arguments[0].click();", yes_terms_element)
                terms_of_use = False
            time.sleep(2)
            driver.find_element_by_xpath("//body").click()
            print(f'Email {i+1} generated successfully!')

        except Exception as e:
            print(f'Error: {e}')    

generate_emails()
