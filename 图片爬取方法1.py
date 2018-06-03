import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }


dowmload_links = []
path = 'C://Users/wucaoyue/Pictures/Camera Roll/'
url = 'http://www.mzitu.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
imgs = soup.select('li > a > img')
for img in imgs:
    print(img.get('data-original'))
    dowmload_links.append(img.get('data-original'))
for item in dowmload_links:
    urlretrieve(item,path+item[-10:])