import requests   #导包
import base64
host="http://192.168.3.154:80"  #部署的服务器地址
login_url="/classify"  #请求地址
url=host+login_url #拼接地址
filepath = "1.jpg"
#参数
file = open(filepath, "rb")
txt = base64.b64encode(file.read())
body= txt

#发送请求
r=requests.post(url=url,data=body)
#输出返回
print(r.text)