import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Getting Movie title
title=str(input("What is the movie title\n")).title()
webformatted_title="movie-" + title.replace(" ","%20")+"--hmp4.htm"
search_title=title+" BluRay 720p.mkv"

# Starting webdriver
os.environ['PATH'] +=r"C://seleniumDriver"
driver=webdriver.Edge()

# Opening and working with fzmovies

driver.get(f"https://fzmovies.net/{webformatted_title}")
driver.implicitly_wait(20)
try:
    driver.switch_to.alert.accept()
    driver.find_element(by="css selector",value=".close-button")
except:
    print("Couldn't find element")
time.sleep(20)
element1=driver.find_element(by="id",value="downloadoptionslink2").click()
# driver.switch_to.alert.accept()
driver.implicitly_wait(20)
element2=driver.find_element(by="id",value="downloadlink").click()
driver.implicitly_wait(20)
element3=driver.find_element(by="id",value="dlink1").click()


while True:
    pass

