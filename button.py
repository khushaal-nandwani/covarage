""" The main aim of this py file is to keep track of all the button or things
that we will require while we access the website so that in case they change in future,
we just have to make changes in the <button.py>
"""
from selenium.webdriver.common.by import By

GET_OTP = (By.ID, "mat-input-0")
OTP_TEXTBOX = (By.XPATH, '//div/input[@maxlength="6"]')
OTP_VERIFY = (By.TAG_NAME, "ion-button")

SCHEDULE = (By.XPATH, "//a/span[contains(text(), 'Schedule')]")
SCHEDULE_NOW = (By.TAG_NAME, "ion-button")

SEARCH_SWITCH = (By.CLASS_NAME, "status-switch")

SELECT_STATE = (By.TAG_NAME, "mat-select")

SEARCH = (By.XPATH, "//ion-button[contains(text(), 'Search')]")
AGE18 = (By.XPATH, '//input[@id="c1"]')
# AGE45 = (By.XPATH, '//input[@id="c2"]')
# AGE18 = AGE45
ROWS = '//ul[@class="slots-available-wrap"]'
COL = 'li'
SLOTS = '//div[@class="vaccine-box vaccine-box1 vaccine-padding"]/a'

TIME = (By.CLASS_NAME, 'button')
CAPTCHA = '//input[@placeholder="Enter Security Code"]'
