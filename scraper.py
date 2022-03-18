import requests
from urllib.request import urlparse
from bs4 import BeautifulSoup
from pyparsing import results
import re
import xlsxwriter
import pandas

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}
# url = 'https://www.pexels.com/search/spinach/'
# page = requests.get(url, headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# # test = soup.find_all('img', class_='media-3IiMe', src_='')
# # print(test)



with open('/Users/banegryphon/PycharmProjects/pythonProject1/demofile3.html') as fp:
    soup = BeautifulSoup(fp, 'lxml')
    test = soup.find_all('img', class_='media-3IiMe', src_='')
    test = str(test)
    # print(test)

def getUrl(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


result = str(getUrl(test))
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
writer.save()
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write(result)
#
# workbook.close()
# f = open("demofile3.html", "x")
# f.write(soup.prettify())
# f.close()

# headers = {'User-Agent': 'Mozilla/5.0'}
# request = Request(url, headers=headers)
# html = urlopen(request).read()
# print(html.img)
# soup = BeautifulSoup(url.read(), 'html.parser')
# class="link--h3bPW
#
# for button in soup.find('div', class_="link--h3bP"):
#     print(button)


#---------------TRYING TO READ A FILE-----------------#
# with open("demofile3.html") as f:
#     soup = BeautifulSoup(f.read(), 'html.parser')
#     image_tags = soup.find('img src', class_='media-3IiMe').text
#     print(image_tags)


#---------CREATING AND WRITING A FILE TO CONTAIN THE SCRAPE CODE----------#

# f = open("demofile3.txt", "x")
# f.write(soup.prettify())
# f.close()
#--------------------------------------------------------------------------#

# print(soup.prettify())
# links = []




# howFavoriteWrapper-21vlX showPreviewWrapper-2o1ut assetWrapper-2LqKz descriptionWrapper-i6Ter assetWrapper-O9SHq
# media-3IiMe
# for image_tag in image_tags:
#     links.append(image_tag['src'])


# warning = soup.find ('div', class_="hide-featured-badge hide-favorite-badge")
# book_container = warning.nextSibling
# images = book_container.findAll('img')

# req = urlopen('https://www.canstockphoto.com/images-photos/spinach.html')
# webpage = BeautifulSoup(req.read(), 'html.parser')
# print(webpage)
#
# url = 'https://www.canstockphoto.com/images-photos/spinach.html'
# headers = {'User-Agent': 'Mozilla/5.0'}
# request = Request(url, headers=headers)
# html = urlopen(request).read()
# print(html.img)
# soup = BeautifulSoup(url.read(), 'html.parser')
# class="link--h3bPW
#
# for button in soup.find('div', class_="link--h3bP"):
#     print(button)
#
#
# URL = "https://www.dreamstime.com/photos-images/spinach-field.html"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
# aas = soup.find_all("div", class_="dt-image")
#
# print(aas)
#
# #for test in aas:
#     #image_tag = test.findChildren("img")
#     #image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))
#     #print(test)
# #for item in soup.find_all('img src'):
#    # print(item)

