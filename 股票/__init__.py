import csv
import os
import time

import requests
from PIL.features import codecs
from lxml import etree
import re
def GetHtmlText(name):
    url_list = ["http://quotes.money.163.com/trade/lsjysj_"+str(name)+".html?year=2020&season=3","http://quotes.money.163.com/trade/lsjysj_"+str(name)+".html?year=2020&season=2","http://quotes.money.163.com/trade/lsjysj_"+str(name)+".html?year=2020&season=1","http://quotes.money.163.com/trade/lsjysj_"+str(name)+".html?year=2019&season=4","http://quotes.money.163.com/trade/lsjysj_"+str(name)+".html?year=2019&season=3"]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_ntes_nnid=65757f7e2bd0dece39d402324b1d9cd9,1592287490262; _ntes_nuid=65757f7e2bd0dece39d402324b1d9cd9; vjuids=-12b7c84e3.17348173187.0.2db48e565b742; vjlast=1594642346.1594642346.30; ne_analysis_trace_id=1594642836774; s_n_f_l_n3=176e5a7266b6ff111594642836782; NNSSPID=30a0420785ee415885a6b37657923e18; _ntes_stock_recent_=1000002%7C1002016%7C1300059%7C0601398%7C1002845; _ntes_stock_recent_=1000002%7C1002016%7C1300059%7C0601398%7C1002845; _ntes_stock_recent_=1000002%7C1002016%7C1300059%7C0601398%7C1002845; vinfo_n_f_l_n3=176e5a7266b6ff11.1.0.1594642836781.0.1594643802464',
        'Host': 'quotes.money.163.com',
        'Referer': 'http://quotes.money.163.com/trade/lsjysj_002230.html?year=2020&season=4',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',    }
    for url in url_list:
        respon = requests.get(url=url,headers=headers)
        print(respon.status_code)
        respon.encoding = 'utf-8'
        html = etree.HTML(respon.text)
        riqi = html.xpath('//td[1]/text()')
        kaipanjia = html.xpath('//td[2]/text()')
        zuigaojia = html.xpath('//td[3]/text()')
        zuidijia = html.xpath('//td[4]/text()')
        shoupanjia = html.xpath('//td[5]/text()')
        zhangdiee = html.xpath('//td[6]/text()')
        zhangdiefu = html.xpath('//td[7]/text()')
        chengjiaoliang = html.xpath('//td[8]/text()')
        chengjiaojinge = html.xpath('//td[9]/text()')
        zhenfu = html.xpath('//td[10]/text()')
        huanshoulv = html.xpath('//td[11]/text()')
        global info_riqi
        info_riqi = []
        for i in riqi:
            # 正则表达式提取列表里面需要的元素
            if re.match("\d+\.?\d*", i) is not None:
                info_riqi.append(i)
        print(len(info_riqi))
        global info_zuigaojia
        info_zuigaojia = []
        for i in zuigaojia:
            if re.match("\d+\.?\d*", i) is not None:
                info_zuigaojia.append(i)
        print(len(info_zuigaojia))
        global info_kaipanjia
        info_kaipanjia = []
        for i in kaipanjia:
            if re.match("\d+\.?\d*", i) is not None:
                info_kaipanjia.append(i)
        print(len(info_kaipanjia))
        global info_zuidijia
        info_zuidijia = []
        for i in zuidijia:
            if re.match("\d+\.\d+", i) is not None:
                info_zuidijia.append(i)
        print(len(info_zuidijia))
        global info_shoupanjia
        info_shoupanjia = []
        for i in shoupanjia:
            if re.match("\d+\.\d+", i) is not None:
                info_shoupanjia.append(i)
        print(len(info_shoupanjia))
        global info_zhangdiee
        info_zhangdiee = []
        for i in zhangdiee:
            if re.match("[-]?\d+\.\d+", i) is not None:
                info_zhangdiee.append(i)
        print(len(info_zhangdiee))
        global info_zhangdiefu
        info_zhangdiefu = []
        for i in zhangdiefu:
            if re.match("[-]?\d+\.\d+", i) is not None:
                info_zhangdiefu.append(i)
        print(len(info_zhangdiefu))
        global info_chengjiaoliang
        info_chengjiaoliang = []
        for i in chengjiaoliang:
            if re.match("[1-9]\d*", i) is not None:
                info_chengjiaoliang.append(i)
        print(len(info_chengjiaoliang))
        global info_chengjiaojinge
        info_chengjiaojinge = []
        for i in chengjiaojinge:
            if re.match("[1-9]\d*", i) is not None:
                info_chengjiaojinge.append(i)
        print(len(chengjiaojinge))
        global info_zhenfu
        info_zhenfu = []
        for i in zhenfu:
            if re.match("\d+\.\d+", i) is not None:
                info_zhenfu.append(i)
        print(len(zhenfu))
        global info_huanshoulv
        info_huanshoulv = []
        for i in huanshoulv:
            if re.match("\d+\.\d+", i) is not None:
                info_huanshoulv.append(i)
        print(len(info_huanshoulv))
        WirteFile(name)
# 写入文件
def WirteFile(name):
    filepath = os.path.join(read_dir, str(name)+'.csv')
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        dictWriter = csv.writer(f)
        dictWriter.writerow(['公司编码', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌额', '涨跌幅', '成交量', '成交金额', '振幅', '换手率'])
        for i in range(len(info_riqi)):
            dictWriter.writerow(
                [name, info_riqi[i], info_kaipanjia[i], info_zuigaojia[i], info_zuidijia[i], info_shoupanjia[i],
                 info_zhangdiee[i], info_zhangdiefu[i], info_chengjiaoliang[i], info_chengjiaojinge[i], info_zhenfu[i],
                 info_huanshoulv[i]])
if __name__ == '__main__':
    read_dir = os.path.join(os.curdir, '公司股票信息')
    if not os.path.isdir(read_dir):
        os.mkdir(read_dir)
    Dict = {}
    name_list = ['002626','002650','603299','603027','603696','300401','300146','603043','600597','600882','300829','603317','600305','603288','603020','002216','600929','002847','600429','603886','002956','002507','300858','600872','600887','002732','603866','603697','600419','603079','002770','600866','000716','300765','002719','600186','002661','300791','002802','002481','600298','002053','002495','603755','600073','002910','600873','002946','688089','603739','600381','002570','002329']
    for name in name_list:
        GetHtmlText(name)
        time.sleep(0.1)