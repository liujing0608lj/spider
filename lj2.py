import urllib.request
import urllib.parse

def search(parsmeters)

data =  urllib.parse.urlencode(parameters)
print(data)

request_ = urllib.request.Request(url='http://www.baidu.com/s?'+data
 ,method="GET")
response = urllib.request.urlopen(request_)
print(response.url)
HTML=response.read().decode()
print(HTML)
with open("/home/ubuntu/Desktop/lj2.txt",mode='w') as f:
    f.write(HTML)

def main():
    pars={
        "wd":"胡旺是个好人"
    }