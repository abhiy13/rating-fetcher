import sys
import requests
from bs4 import BeautifulSoup as BS

def get_rating(username):
  url = 'https://www.codechef.com/users/' + username
  page = requests.get(url)
  soap = BS(page.text , 'html.parser')

  ratings = soap.find_all('div' , class_ = 'rating-container')
  rat = ratings[0]
  x = rat.a.text
  p = x.split(' ')
  return p[0]
#  print("Recent Increase {}".format(p[1]))


if(len(sys.argv) > 1): 
  if((sys.argv[1]) == 'test'):
    print(get_rating('pieliedie'))
