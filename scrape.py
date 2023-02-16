import requests 
import urllib.request
from bs4 import BeautifulSoup
URL = "https://www.google.com/search?q=Innovators+by+Walter+Issacson&sxsrf=ALeKk03xBalIZi7BAzyIRw8R4_KrIEYONg:1620885765119&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjv44CC_sXwAhUZyjgGHSgdAQ8Q_AUoAXoECAEQAw&cshid=1620885828054361"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
image_tags = soup.find_all('img', class_='yWs4tf')
links = []
#print(image_tags)
for image_tag in image_tags:
    links.append(image_tag['src'])
 
print(len(links))
num = 0
for l in links :
	urllib.request.urlretrieve(l, "images/innovator"+'{num}'+".jpg")
	num += 1
