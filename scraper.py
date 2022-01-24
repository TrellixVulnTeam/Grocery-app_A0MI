import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pyparsing import results


#req = urlopen('https://www.canstockphoto.com/images-photos/spinach.html')
#webpage = BeautifulSoup(req.read(), 'html.parser')
#print(webpage)

#url = 'https://www.canstockphoto.com/images-photos/spinach.html'
#headers = {'User-Agent': 'Mozilla/5.0'}
#request = Request(url, headers=headers)
#html = urlopen(request).read()
#print(html.img)
#soup = BeautifulSoup(url.read(), 'html.parser')
#class="link--h3bPW

#for button in soup.find('div', class_="link--h3bP"):
    #print(button)


URL = "https://www.dreamstime.com/photos-images/spinach-field.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
aas = soup.find_all("div", class_="dt-image")

print(aas)

#for test in aas:
    #image_tag = test.findChildren("img")
    #image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))
    #print(test)
#for item in soup.find_all('img src'):
   # print(item)

