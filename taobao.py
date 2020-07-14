from idlelib import browser
from selenium import webdriver
import datetime
import time


def login():
    # Login via Wechat
    browser.get("https://passport.jd.com/uc/login?ltype=logout&ReturnUrl=https://global.jd.com/")
    time.sleep(2)
    if browser.find_element_by_link_text("微信"):
        browser.find_element_by_link_text("微信").click()
        print("Please login within 6 sec")
        time.sleep(6)


def picking():
    # Open your cart
    browser.get("https://cart.jd.com/cart.action#none")
    time.sleep(2)


def checklist():
    try:
        if browser.find_element_by_xpath("//div[@class='amount-sum']/em[text()=\"0\"]"):
            time.sleep(3)
            print("Please select one item at least")
            checklist()
    except:
        pass


def order(times):
    if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > times:
        browser.find_element_by_link_text("去结算").click()
    else:
        order(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


if __name__ == "__main__":
    # Set start time，time format："2019-06-01 10:08:00.000"
    t = "2020-07-14 15:55:00.000"
    # Open Chrome
    browser = webdriver.Chrome()
    # maximize Chrome window
    browser.maximize_window()
    # Login website
    login()
    # Open your cart
    picking()
    # Check cart
    checklist()
    # Place your order
    order(t)
