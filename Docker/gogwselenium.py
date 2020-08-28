#!/usr/local/bin/python3
from decimal import *
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys


# Initiate webdriver to use with Firefox, use a different driver to use with a different browser.
try:
  driver=webdriver.Firefox()
except:
  path = input('geckodriver is not in your path, please type the path to the geckodriver executable: ')
  driver=webdriver.Firefox(executable_path=path)

def get_driver():
  # The username is concatenated into the url and the request is made to find its wishlist.
  # username is obtained as the first argument called
  try:
    url = "https://www.gog.com/u/"+sys.argv[1]+"/wishlist"
  except:
    username = input("please type a username: ")
    url = "https://www.gog.com/u/"+username+"/wishlist"
  driver.get(url)
  return driver
    

def process_data(driver):
  # Extracting the avatar through class avatar avatar--small avatar--in-text
  avatar = driver.find_element_by_class_name("user__avatar-container")
  # Clearing the links so that only the ones contained in scrset appear instead of the whole class
  aux_avatar = avatar.find_element_by_tag_name("img")
  avatar_links = aux_avatar.get_attribute('srcset')
  try:
    nav_list = driver.find_element_by_class_name("list-navigation__pagin")
    # Number of Pages contains the total number of pages that contain the wishlist  
    number_of_pages = nav_list.find_element_by_class_name("pagin__total").text
  except:
    number_of_pages = 1
  all_games = []
  all_prices = []
  total_price = 0
  for page in range(int(number_of_pages)):
    games = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class = 'product-title__text'][@ng-bind = '::product.title']")))
    # Add each game title as a string to the allGames list
    for game in games:
      all_games.append(game.text)

    # Search the price by xpath (it's the only way found to obtain a webdriver object that could return text)
    prices = driver.find_elements_by_xpath("//span[@class = '_price product-state__price'][@ng-bind = 'product.price.amount']")
    # For each element, check if the price exists (is not "TBA", "owned" or "free")
    # If it does, turn it into a decimal and add it to the total price
    for price in prices:
      if price.text == '':
        all_prices.append('0')
        continue
      else:
        all_prices.append(price.text)
        total_price += (Decimal(price.text))

    # Search for the element that contains the "pagin__next" text within the "list navigation pagin" object and press it
    try:
      nav_list.find_element_by_class_name("pagin__next").click()
    except:
      continue
  #totalPrice = sum(allPrices)
  driver.quit()
  return avatar_links, all_games, all_prices, total_price

# Save the avatar links, the games and prices and the total price as dictionaries into a json file
def save_json_file(avatar_links, games, prices, total_price):
  avatars = {'Avatar links': avatar_links}
  numbers = {'Total number of games': len(games)}
  data = dict(zip(games, prices))
  final_price = {'Total price': str(total_price)}
  final_list = [avatars, numbers, data, final_price]
  with open('data.json', 'w') as outfile:
      json.dump(final_list, outfile, sort_keys=True, indent=4)


def main():
  driver = get_driver()
  avatar_links, games, prices, total_price = process_data(driver)
  save_json_file(avatar_links, games, prices, total_price)


if __name__ == "__main__":
  main()