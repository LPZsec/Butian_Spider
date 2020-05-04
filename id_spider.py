# -*-coding:utf-8 -*-
import requests, json, re

url = "https://www.butian.net/Reward/pub"
header = \
	{
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
		"Accept":"application/json, text/javascript, */*; q=0.01",
		"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		"Accept-Encoding":"gzip, deflate",
		"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
		"X-Requested-With":"XMLHttpRequest",
		"Content-Length":"16",
		"Origin":"https://www.butian.net",
		"Connection":"close",
		"Referer":"https://www.butian.net/Reward/plan"
	}

patten = re.compile(r"d': u'\d*")

def ansy(data_id):
	a = []
	r = re.findall(patten, data_id)
	for i in r:
		a.append(i[6:])
	return a

def spider(i):
	data = {"s":1,"p":i,"token":""}
	response = requests.post(url, headers=header, data=data)
	
	try:
		data_id = json.loads(response.text)
	except Exception as e:
		print("爬取第"+str(i)+"页异常，正在重连")
		return spider(i)

	return ansy(str(data_id))

def main(filename):
	file = open(filename, "w+")
	for i in range(1,183):
		a = spider(i)
		print("正在爬取第 "+ str(i) +" 页")
		for i in a:
			file.write(i)
			file.write("\n")
	file.close()
	print("finish")
