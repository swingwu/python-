import requests
import re

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
info_lists = []  # 初始化列表，用于装取爬虫信息


def judgment_sex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'


def get_info(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)Icon">32</div>', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(>*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i>', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {'id': id,
                'level': level,
                'sex': judgment_sex(),
                'content': content,
                'laugh': laugh,
                'comment': comment
                }
        info_lists.append(info)

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    for url in urls:
        get_info(url)
    for info_list in info_lists:
        f = open('C:/Users/wucaoyue/Desktop/qiushi.txt', 'a+')  # 新建txt文档，追加的方式
        f.write(info_list['id'] + '\n')
        f.write(info_list['level'] + '\n')
        f.write(info_list['sex'] + '\n')
        f.write(info_list['content'] + '\n')
        f.write(info_list['laugh'] + '\n')
        f.write(info_list['comment'] + '\n')
        f.close()

