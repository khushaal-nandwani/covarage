import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import button
import input

# set up

PATH = r"C:\Users\Nandw\Downloads\Installerts\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://selfregistration.cowin.gov.in/")
# driver.maximize_window()

def click_search_button():
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(button.SEARCH))
    time.sleep(0.1)
    search_button.click()


def click_age_button():
    age_18 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(button.AGE18)
    )
    driver.execute_script("arguments[0].click();", age_18)


def scan_for_available_slots_click_available() -> bool:
    all_slots = driver.find_elements_by_xpath(button.SLOTS)
    for slot in all_slots:
        slot_text = slot.text.strip()
        if slot_text.isnumeric():
            available_slot_path = '//div[@class="vaccine-box vaccine-box1 vaccine-padding"]/a[contains(text(), ' + slot.text + ')]'
            available_slot = driver.find_element_by_xpath(available_slot_path)
            driver.execute_script("arguments[0].click();", available_slot)
            return True
    return False

 
enter_mobile_number = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located(button.GET_OTP)
)

enter_mobile_number.send_keys(input.MOBILE_NUMBER)
enter_mobile_number.send_keys(Keys.TAB, Keys.RETURN)

OTP_enter = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located(button.OTP_TEXTBOX)
)
OTP_enter.send_keys(Keys.SPACE)


schedule_button = WebDriverWait(driver, 1000).until(
    EC.presence_of_element_located(button.SCHEDULE)
)
driver.execute_script("arguments[0].click();", schedule_button)
"""
schedule_now = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(button.SCHEDULE_NOW)
)
wait2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(button.SCHEDULE_NOW)
)
time.sleep(0.5)
schedule_now.click()
"""      # no more needed in new version

search_switch = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(button.SEARCH_SWITCH)
)
driver.execute_script("arguments[0].click();", search_switch)

state = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(button.SELECT_STATE)
)

time.sleep(0.4)
state.send_keys(input.STATE)
state.send_keys(Keys.RETURN)

time.sleep(0.3)

district = driver.find_element_by_xpath(
    '//mat-select[@formcontrolname="district_id"]')
district.send_keys(input.DISTRICT)
district.send_keys(Keys.RETURN)

click_search_button()
click_age_button()

time.sleep(1)

booking_confirmed = scan_for_available_slots_click_available()

while not booking_confirmed:
    click_search_button()
    click_age_button()
    time.sleep(0.5)
    booking_confirmed = scan_for_available_slots_click_available()

time.sleep(0.2)

time_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'appoint-success'))
)

time_buttons = driver.find_elements(*button.TIME)
driver.execute_script("arguments[0].click();", time_buttons[1])

time.sleep(.5)
captcha_area = driver.find_element_by_xpath(button.CAPTCHA)
captcha_area.send_keys("")
