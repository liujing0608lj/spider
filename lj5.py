import requests

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
t = response.text
l1 = t.split('\r\n')
#print(len(l1))
for i in l1:
    print(i)

for url_ in l1:
    try:
        response_ = requests.get(url_,timeout = 1,allow_redirects=False) 
        print(response_.status_code)
        print(response_.content)
    except:
        print('Timeout')
    else:
        with open("/home/ubuntu/Desktop/"+url_.split('/')[-1],'wb') as f:
            f.write(response_.content)


