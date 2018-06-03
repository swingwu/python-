import requests
import re
import time

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
f=open('C:/Users/wucaoyue/Desktop/dopo.txt','a+') #新建txt文档，追加的方式

def get_info(url):
    res=requests.get(url,headers=headers)
    if res.status_code==200:
        contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
    else:
        pass

if __name__=='__main__':
    urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,1665)]
    for url in urls:
        get_info(url) #循环调用get_info函数
        time.sleep(1)

f.close()  #关闭txt文件
