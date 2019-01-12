import urllib.request   #python

response = urllib.request.urlopen("http://www.17k.com/chapter/2933095/36699279.html")
print(response)
#print(dir(response))
#print(response.read())
print("*****************************************************************")
with open('/home/ubuntu/Desktop/lj1.txt','w',encoding='utf8') as f:
    f.write(response.read().decode('utf8'))