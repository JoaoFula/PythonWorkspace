# import lybraries
import requests
from bs4 import BeautifulSoup
import re
from decimal import *
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Initiate webdriver to use with Firefox, use a different driver to use with a different browser.
options = Options()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Firefox(executable_path='C:\Joao\gecko\geckodriver.exe')


def get_driver(username):
  # This username is concatenated into the url and the request is made to find its wishlist
  url = "https://www.gog.com/u/"+username+"/wishlist"
  driver.get(url)
  return driver
    

def process_data(driver):
  # Extracting the avatar through class avatar avatar--small avatar--in-text
  avatar = driver.find_element_by_class_name("user__avatar-container")
  # Clearing the links so that only the ones contained in scrset appear instead of the whole class
  auxAvatar = avatar.find_element_by_tag_name("img")
  avatarLinks = auxAvatar.get_attribute('srcset')
  try:
    navList = driver.find_element_by_class_name("list-navigation__pagin")
    # Number of Pages contains the total number of pages that contain the wishlist  
    NumberOfPages = navList.find_element_by_class_name("pagin__total").text
  except:
    NumberOfPages = 1
  allGames = []
  allPrices = []
  totalPrice = 0
  for page in range(int(NumberOfPages)):
    games = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class = 'product-title__text'][@ng-bind = '::product.title']")))
    # Add each game title as a string to the allGames list
    for game in games:
      allGames.append(game.text)

    # Search the price by xpath (it's the only way found to obtain a webdriver object that could return text)
    prices = driver.find_elements_by_xpath("//span[@class = '_price product-state__price'][@ng-bind = 'product.price.amount']")
    # For each element, check if the price exists (is not "TBA", "owned" or "free")
    # If it does, turn it into a decimal and add it to the total price
    for price in prices:
      if price.text == '':
        allPrices.append('0')
        continue
      else:
        allPrices.append(price.text)
        totalPrice += (Decimal(price.text))

    # Search for the element that contains the "pagin__next" text within the "list navigation pagin" object and press it
    try:
      navList.find_element_by_class_name("pagin__next").click()
    except:
      continue
  #totalPrice = sum(allPrices)
  driver.quit()
  return avatarLinks, allGames, allPrices, totalPrice

# Save the avatar links, the games and prices and the total price as dictionaries into a json file
def save_json_file(avatarLinks, games, prices, totalPrice):
  avatars = {'avatarLinks': avatarLinks}
  numbers = {'Total number of games': len(games)}
  data = dict(zip(games, prices))
  FinalPrice = {'Total price': str(totalPrice)}
  with open('data.json', 'w') as outfile:
      json.dump(avatars, outfile)
      json.dump(numbers, outfile)
      json.dump(data, outfile)
      json.dump(FinalPrice, outfile)


def main():
  username = input('Type the username: ')
  driver = get_driver(username)
  avatarLinks, games, prices, totalPrice = process_data(driver)
  save_json_file(avatarLinks, games, prices, totalPrice)


if __name__ == "__main__":
  main()