import requests
from lxml import etree
import pymysql
from multiprocessing import Pool

conn=pymysql.connect(host='localhost',user='root',password='123456',db='mydb',port=3306,charset='utf8')
cursor=conn.cursor()


def get_jianshu_info(url):
    html=requests.get(url)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="note-list"]/li')  #获取大标签，以此循环

    for info in infos:
        try:
            author=info.xpath('/div/div[1]/div/a/text()')[0]
            time=info.xpath('/div/div[1]/div/span/@data-shared-at')[0]
            title=info.xpath('/div/a/text()')[0]
            content=info.xpath('/div/p/text()')[0].strip()
            view=info.xpath('/div/div[2]/a[1]/text()')[1].strip()
            comment=info.xpath('/div/div[2]/a[2]/text()')[1].strip()
            like=info.xpath('/div/div[2]/span[2]/text()')[0].strip()
            rewards=info.xpath('/div/div[2]/span[3]/text()')
            if len(rewards)==0:
                reward='无'
            else:
                reward=rewards[0].strip()
            data={
                'author':author,
                'time':time,
                'title':title,
                'content':content,
                'view':view,
                'comment':comment,
                'like':like,
                'reward':reward
            }
            cursor.execute('use mydb')
            tb=cursor.execute('create table jianshu_shouye（author,time,title,content,view,comment,like,rewards)')
            cursor.execute(tb)
            sql="insert into jianshu_shouye values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(str(author),str(time),str(title),str(content),str(view),str(comment),str(like),str(rewards)))
                 #插入数据库
            conn.commit()
            conn.close()

        except IndexError:
            pass


if __name__=='__main__':
    urls=['https://www.jianshu.com/c/bDHhpk?order_by=commented_at&page={}'.format(str(i)) for i in range(1,10001)]
    pool=Pool(processes=4)#创建进程池
    pool.map(get_jianshu_info,urls)#调用进程爬虫





