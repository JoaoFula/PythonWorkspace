# import lybraries
import requests
from bs4 import BeautifulSoup
import re
from decimal import *
import json


def get_soup(username):
    # This username is concatenated into the url and the request is made to find its wishlist
    url = "https://www.gog.com/u/"+username+"/wishlist"
    page = requests.get(url)
    

    # Get the response code and turn the content in page into a beautiful soup object
    if page.status_code == requests.codes.ok:
        print("Connected")
        soup = BeautifulSoup(page.text, 'html.parser')
        with open("API/wishlist.html", 'wb') as fd:
            for chunk in page.iter_content(chunk_size=128):
                fd.write(chunk)
       
        return soup
    else:
        print("Not connected, check wishlist viewing permissions")
        return 0

    

def process_data(soup):
    # Extracting the avatar through class avatar avatar--small avatar--in-text
    avatar = soup.find('img', class_="avatar avatar--small avatar--in-text")
    # Clearing the links so that only the ones contained in scrset appear instead of the whole class
    avatarLinks = avatar.get('srcset')
    # Extract the text/javascript that contains the information regarding the games on the wishlist and the prices
    text = soup.find('script', type="text/javascript")
    games = re.findall('"title":"(.*?)"', str(text))
    prices = re.findall('"finalAmount":"(.*?)"', str(text))
    totalPrice = 0
    for price in prices:
        price = Decimal(price) # There is a decimal part to the string therefore the decimal library is needed
        totalPrice = totalPrice + price


    return avatarLinks, games, prices, totalPrice

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
    soup = get_soup(username)
    if soup == 0:
        print('Error, not possible to continue.')
    avatarLinks, games, prices, totalPrice = process_data(soup)
    save_json_file(avatarLinks, games, prices, totalPrice)


if __name__ == "__main__":
    main()