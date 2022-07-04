#!usr\bin\python
##########################################################################################################################################
#Name : Eugene Martins
#Date : 10/6/2022
# lesson: Web scraping
###############################################################################################################################################
import requests

from bs4 import BeautifulSoup as bs
user_name = "malobaeugene"#input(Enter your username)
url = "https://github.com/" + user_name#input(Enter site url)
results = requests.get(url)

soup = bs(results.content,'html.parser')
profile_pic = soup.find("img",{'alt':'avatar rounded-2 avatar-user'})
print(profile_pic)