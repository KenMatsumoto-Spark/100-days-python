from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

LINKEDIN_EMAIL = ""
LINKEDIN_PASS = ""
PHONE = ""

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

login_button = driver.find_element_by_css_selector(".nav__button-secondary")
login_button.click()

time.sleep(5)
username = driver.find_element_by_name("session_key")
username.send_keys(LINKEDIN_EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(LINKEDIN_PASS)
password.send_keys(Keys.ENTER)


# #Locate the apply button
# time.sleep(5)
# apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
# apply_button.click()
#
# #If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element_by_class_name("fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE)
#
# #Submit the application
# submit_button = driver.find_element_by_css_selector("footer button")
# submit_button.click()


all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()