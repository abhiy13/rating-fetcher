import sys
import requests
from bs4 import BeautifulSoup as BS

def get_rating(username):
  url = 'https://codeforces.com/profile/' + username
  page = requests.get(url)
  soap = BS(page.text , 'html.parser')
  '''
  print(soap)
  with open("cftour.txt" , "w") as fo:
    for text in soap:
      fo.write(str(text))
  '''
  ratings = soap.find_all('span')
  rat = ratings
  ar = []
  for i in rat:
    if("user-" in str(i) and "font-weight:bold" in str(i)):
      ar.append(i.text)
  return ar[0]


if(len(sys.argv) > 1): 
  if((sys.argv[1]) == '--test'):
    print(get_rating('abhiroxx'))
