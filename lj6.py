import requests
from lxml import etree
import pymongo

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
for num in range(1,4):
    if num == 1:
        response = requests.get('http://op.hanhande.net/shtml/meitu.shtml',headers = headers)
    else:
        response = requests.get('http://op.hanhande.net/shtml/op_wz/list_2602_{}.shtml'.format(num),headers = headers)
    response.encoding = 'gbk'
    tree = etree.HTML(response.text)
    res=tree.xpath('//*[@id="main"]/div[2]/div[2]/ul/li/a/img') 
    
    for a in res:
        src = (a.xpath('./@src')[0])
      
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["hh"]
        mycol = mydb["xpath"]
        mycol.insert_one({'url':src})
        myclient.close() 