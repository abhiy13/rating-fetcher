import sys
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver 

def get_rating(username):
  url = 'https://www.hackerrank.com/' + username
  driver = webdriver.Firefox()
  driver.get(url)
  page = driver.page_source
  soap = BS(page)
#  print(soap)
  with open("hrank.html" , "w") as fo:
    for text in soap:
      fo.write(str(text))
  am = soap.findAll('h6')
  userrat = []
  for i in am:
#    print(i , i.text)
    if("ContestRating:" in str(i)):
      userrat.append(i.text)
#      print(i)
  return (userrat[0]).replace("ContestRating:" , "")
'''
  ratings = soap.find_all('div' , class_ = 'rating-container')
  rat = ratings[0]
  x = rat.a.text
  p = x.split(' ')
  print(p[0], sep = " ")
  print("Recent Increase {}".format(p[1]))
'''
if(len(sys.argv[1]) == 'test'):
  print(get_rating('AbhiY13'))