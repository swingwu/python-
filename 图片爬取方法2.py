import requests
from lxml import etree

urls=['http://www.mzitu.com/page/{}/'.format(str(i)) for i in range(1,20)]
path='C://Users/wucaoyue/Pictures/Camera Roll/'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
def get_photo(url):
    html=requests.get(url)
    selector=etree.HTML(html.text)
    photo_urls=selector.xpath('//*[@id="pins"]/li/a/img/@href')
    for photo_url in photo_urls:
        data=requests.get(photo_url,headers=headers)
        fp=open(path + photo_url[-10:],'wb')
        fp.write(data.content)
        fp.close()
for url in urls:
    get_photo(url)