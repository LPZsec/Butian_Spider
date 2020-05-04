# -*- coding: utf-8 -*-
import requests, re, time, os, id_spider

url = 'https://www.butian.net/Loo/submit?cid='
# n_patten = re.compile(r'厂商" value="([\u4E00-\u9FA5]+)')
do_patten = re.compile(r'隔" value="([^\s]*)"')

def spider(num):
	timestamp = str(int(round(time.time() * 1000)))
	headers = \
	{
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
		"Accept":"application/json, text/javascript, */*; q=0.01",
		"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		"Accept-Encoding":"gzip, deflate",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "navigate",
		"Sec-Fetch-User": "?1",
		"Sec-Fetch-Dest":"document",
		"Referer":"https://www.butian.net/Company/"+str(num),
	}
	cookies = \
		{
			# ---------------------------
			# 修改为自己的cookie
			# ---------------------------
			"__q__":timestamp
		}

	s_url = url + str(num)
	try:
		res_text = requests.get(s_url,headers=headers, cookies=cookies).text.encode("utf8")
		domain = re.findall(do_patten, res_text)
	except Exception as e:
		print("服务器拒绝了请求，正在重试")
		time.sleep(1)
		spider(num)
	if not(domain[0]):
		print("正在重连 请稍后")
		spider(num)
	return domain[0]

def test(url):
	response = requests.get(url)
	if response.status_code==502:
		return True
def main():
	id_file = "id.txt"
	if not(os.path.isfile(id_file)):
		id_spider.main(id_file)
	file = open("domain.txt", "w+")
	id_list = open(id_file, "r")

	for num in id_list:
		num = int(num)
		print("正在爬取ID "+str(num)),
		targrt_url = spider(num)
		file.write(targrt_url)
		file.write("\n")
		print(targrt_url)

	file.close()
	id_list.close()
	print("爬取完成")

main()